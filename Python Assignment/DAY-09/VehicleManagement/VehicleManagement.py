from ElectricVehicle import ElectricVehicle
from GasVehicle import GasVehicle
from HybridVehicle import HybridVehicle

ele_car = ElectricVehicle('Nissan', 'Leaf', 2022, 60)
gas_car = GasVehicle('BMW', '3-Series', 2023, 'GASOLINE')
hy_car = HybridVehicle('Lexux', 'NX-Hybrid', 2024, 50, 'Petrol')

print('Electric Vehicle Information : ')
ele_car.display_info()

print('Gas Vehicle Information : ')
gas_car.display_info()

print('Hybrid Vehicle Information : ')
hy_car.display_info()

