from Car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year, color, num_doors, battery_capacity):
        super().__init__(make, model, year, color, num_doors)
        self.__battery_capacity = battery_capacity

    def get_battery_capacity(self):
        return self.__battery_capacity

    def set_battery_capacity(self, battery_capacity):
        self.__battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print("Battery Capacity:", self.__battery_capacity)