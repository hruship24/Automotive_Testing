from Training.StuPers import StuPers


class StudMarks(StuPers):
    def __init__(self, rno, name, dept, sem, mark1, mark2, mark3):
        super().__init__(rno, name, dept, sem)
        self.__mark1 = mark1
        self.__mark2 = mark2
        self.__mark3 = mark3

    def get_mark1(self):
        return self.__mark1
    def set_mark1(self,val):
        self.__mark1 = val

    def get_mark2(self):
        return self.__mark2
    def set_mark2(self,val):
        self.__mark2 = val

    def get_mark3(self):
        return self.__mark3
    def set_mark3(self,val):
        self.__mark3 = val

    def calculate_score(self):
        total = self.__mark1 + self.__mark2 + self.__mark3
        avg = total / 3
        return  total, avg