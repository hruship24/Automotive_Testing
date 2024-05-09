from Training.Animals import Animals
from Training.Fishes import Fishes


class Amphibians(Animals, Fishes):
    def __init__(self, name, legs, tail, fname, ffins, ftail, amname):
        super().__init__(name, legs, tail)
        Fishes.__init__(self, fname, ffins, ftail)
        self.__amname = amname

    def get_aname(self):
        return  self.__amname

    def display(self):
        return  self.get_aname()