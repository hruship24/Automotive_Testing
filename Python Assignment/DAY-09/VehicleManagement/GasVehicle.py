from Vehicle import Vehicle


class GasVehicle(Vehicle):

    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.__fuel_type = fuel_type

    def get_fuel_type(self):
        return self.__fuel_type

    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type
        
    def display_info(self):
        super().display_info()
        print("fuel_type:", self.__fuel_type)
