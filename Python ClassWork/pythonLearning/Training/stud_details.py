class Student :
    def __init__(self, roll_no, name, mo_no):
        self.__roll_no = roll_no
        self.__name = name
        self.__mo_no = mo_no
        self.__total =0

    def get_roll_no(self):
        return self.__roll_no
    def set_roll_no(self,value):
        self.__roll_no=value


    def total_score(self,mark1, mark2, mark3):
        self.__total = mark1 + mark2 + mark3
        return self.__total
