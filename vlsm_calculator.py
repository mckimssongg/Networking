from ipaddress import IPv4Network
import math

def needed_host_bits(number_of_hosts):
    """
    Calculate the minimum number of host bits required to support the specified number of hosts in a subnet.

    Parameters:
    number_of_hosts (int): The number of hosts that the subnet needs to support.

    Returns:
    int: The number of bits needed for the hosts.
    """
    return math.ceil(math.log2(number_of_hosts + 2))  # +2 for network and broadcast addresses


class VLSMCalculator:
    """
    A Variable Length Subnet Mask (VLSM) calculator for subnetting an IP network.

    Attributes:
    base_network (str): The base network in CIDR notation to be subnetted.
    subnets (list): A list of subnet requirements (number of hosts).
    """

    def __init__(self, base_network):
        """
        Constructs all the necessary attributes for the VLSM calculator.

        Parameters:
        base_network (str): The base network in CIDR notation.
        """
        self.base_network = base_network
        self.subnets = []

    def add_subnet(self, name, hosts_required):
        """
        Add a subnet requirement.

        Parameters:
        name (str): The name of the subnet.
        hosts_required (int): The number of hosts required for the subnet.
        """
        self.subnets.append({'name': name, 'hosts': hosts_required})

    def calculate_subnets(self):
        """
        Calculate the subnets based on the base network and the added subnet requirements.

        Returns:
        list: A list of dictionaries, each containing the subnetting information.
        """
        # Sort the subnets by the number of required hosts in descending order
        sorted_subnets = sorted(self.subnets, key=lambda x: x['hosts'], reverse=True)
        current_network = IPv4Network(self.base_network)
        results = []
        available_network = int(current_network.network_address)

        for subnet in sorted_subnets:
            host_bits = needed_host_bits(subnet['hosts'])
            new_prefix = 32 - host_bits
            new_subnet = IPv4Network((available_network, new_prefix))
            available_hosts = (2 ** host_bits) - 2
            first_host = new_subnet.network_address + 1
            last_host = new_subnet.broadcast_address - 1
            results.append({
                'subnet_name': subnet['name'],
                'requested_hosts': subnet['hosts'],
                'network_address': str(new_subnet.network_address),
                'prefix': str(new_subnet.prefixlen),
                'subnet_mask': str(new_subnet.netmask),
                'available_hosts': available_hosts,
                'first_host': str(first_host),
                'last_host': str(last_host),
                'broadcast_address': str(new_subnet.broadcast_address),
            })
            available_network = int(new_subnet.broadcast_address) + 1

        return results
