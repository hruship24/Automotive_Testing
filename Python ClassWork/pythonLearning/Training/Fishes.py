
class Fishes():
        def __init__(self, fname, ffins, ftail):
            self.__fname = fname
            self.__ffins = ffins
            self.__ftail = ftail

        @property
        def get_fname(self):
            return self.__fname

        @get_fname.setter
        def set_fname(self, value):
            self.__fname = value

        @property
        def get_ffins(self):
            return self.__ffins

        @get_ffins.setter
        def set_ffins(self, value):
            self.__ffins = value

        @property
        def get_ftail(self):
            return self.__ftail

        @get_ftail.setter
        def set_ftail(self, value):
            self.__ftail = value

        def displayF(self):
            return  self.__fname, self.__ffins, self.__ftail