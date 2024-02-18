from vlsm_calculator import VLSMCalculator

# Crear una instancia de la calculadora con la red base
vlsm = VLSMCalculator('116.11.9.0/24')

# Agregar las subredes con los hosts requeridos
vlsm.add_subnet('Red 1', 72)
vlsm.add_subnet('Red 2', 50)
# ... agregar más subredes según sea necesario

# Calcular las subredes
subnets = vlsm.calculate_subnets()

# Imprimir los resultados
for subnet in subnets:
    print(subnet)
