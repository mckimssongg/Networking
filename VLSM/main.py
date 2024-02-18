from ipaddress import IPv4Network
import math

# Función para calcular el número mínimo de bits necesarios para soportar una cantidad de hosts
def needed_host_bits(number_of_hosts):
    return math.ceil(math.log2(number_of_hosts + 2))  # +2 por la dirección de red y broadcast

# Función para calcular las subredes ajustada para manejar correctamente la asignación de la siguiente subred
def calculate_subnets_corrected(base_network, subnets):
    # Ordenar las subredes de mayor a menor
    sorted_subnets = sorted(subnets, key=lambda x: x['hosts'], reverse=True)
    current_network = IPv4Network(base_network)
    results = []
    available_network = int(current_network.network_address)

    for subnet in sorted_subnets:
        # Calcular los bits necesarios para hosts
        host_bits = needed_host_bits(subnet['hosts'])
        # Calcular el nuevo prefijo de red
        new_prefix = 32 - host_bits
        # Generar la subred
        new_subnet = IPv4Network((available_network, new_prefix))
        # Calcular el número de hosts disponibles (2^host_bits - 2 por la dirección de red y broadcast)
        available_hosts = (2 ** host_bits) - 2
        # Dirección de inicio y final
        first_host = new_subnet.network_address + 1
        last_host = new_subnet.broadcast_address - 1
        # Agregar los resultados
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
        # Actualizar la dirección de inicio para la próxima subred
        available_network = int(new_subnet.broadcast_address) + 1

    return results

# La red base
base_network = '116.11.9.0/24'

# Las subredes con la cantidad de hosts requeridos
subnets_info = [
    {'name': 'Red 1', 'hosts': 72},
    {'name': 'Red 2', 'hosts': 50},
    {'name': 'Red 3', 'hosts': 18},
    {'name': 'Red 4', 'hosts': 3},
    {'name': 'Red 5', 'hosts': 2},
    {'name': 'Red 6', 'hosts': 2},
    {'name': 'Red 7', 'hosts': 2},
]

# Calcular las subredes con la función corregida
vlsm_subnets_corrected = calculate_subnets_corrected(base_network, subnets_info)
vlsm_subnets_corrected
