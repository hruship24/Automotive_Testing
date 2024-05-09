from Vehicle import Vehicle


class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        Vehicle.__init__(self,make, model, year)
        self.__battery_capacity = battery_capacity

    def get_battery_capacity(self):
        return self.__battery_capacity

    def set_battery_capacity(self, battery_capacity):
        self.__battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print("Battery Capacity:", self.__battery_capacity)