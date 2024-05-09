class College:
    def __init__(self, clgname):
        self.__clgname = clgname

    def get_clgname(self):
        return self.__clgname

    def set_clgname(self, val):
        self.__clgname = val
