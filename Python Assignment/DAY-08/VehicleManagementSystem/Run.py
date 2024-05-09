from Vehicle import Vehicle
from Car import Car
from ElectricCar import ElectricCar

vehicle = Vehicle("Toyota", "Camry", 2022)
vehicle.display_info()
print()

car = Car("Ford", "Focus", 2020, "Red", 4)
car.display_info()
print()

electric_car = ElectricCar("Tesla", "Model S", 2021, "Black", 4, "100 kWh")
electric_car.display_info()
