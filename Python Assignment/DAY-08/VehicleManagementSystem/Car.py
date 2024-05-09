from Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, make, model, year, color, num_doors):
        super().__init__(make, model, year)
        self.__color = color
        self.__num_doors = num_doors

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_num_doors(self):
        return self.__num_doors

    def set_num_doors(self, num_doors):
        self.__num_doors = num_doors

    def display_info(self):
        super().display_info()
        print("Color:", self.__color)
        print("Number of Doors:", self.__num_doors)