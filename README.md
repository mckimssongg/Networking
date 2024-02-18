# Bienvenido a Mis Apuntes de Networking

Este repositorio está dedicado a almacenar y compartir mis apuntes personales y herramientas de networking. Aquí encontrarás una variedad de recursos que van desde simples notas de estudio hasta scripts y librerías útiles para calcular subredes y más.

## Uso de la Librería VLSM Calculator

La librería `vlsm_calculator.py` es una herramienta diseñada para facilitar la creación de esquemas de subnetting VLSM. Para usarla, simplemente importa la clase `VLSMCalculator` en tu script de Python y sigue las instrucciones de uso descritas en los comentarios del código.

Ejemplo de uso:

```python
from vlsm_calculator import VLSMCalculator

vlsm = VLSMCalculator('192.168.1.0/24')
vlsm.add_subnet('Subnet1', 50)
vlsm.add_subnet('Subnet2', 25)
subnets = vlsm.calculate_subnets()

for subnet in subnets:
    print(subnet)
