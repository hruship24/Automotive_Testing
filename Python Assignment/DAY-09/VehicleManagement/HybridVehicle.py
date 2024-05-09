from ElectricVehicle import ElectricVehicle
from GasVehicle import GasVehicle


class HybridVehicle(ElectricVehicle, GasVehicle):
    def __init__(self, make, model, year, battery_capacity,fuel_type):
        ElectricVehicle.__init__(self, make, model, year, battery_capacity)
        GasVehicle.__init__(self, make, model, year, fuel_type)

    def display_info(self):
        super().display_info()
