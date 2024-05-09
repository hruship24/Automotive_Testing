from Training.StudMarks import StudMarks


class StudGrade(StudMarks):
    def __init__(self, rno, name, dept, sem, mark1, mark2, mark3):
        super().__init__(rno, name, dept, sem, mark1, mark2, mark3)
        self.__cgpa =  0

    def get_cgpa(self):
        return self.__cgpa

    def set_cgpa(self,val):
        self.__cgpa = val

    def calculate_cgpa(self):
        total, avg = super().calculate_score()

        if avg >= 80 :
            self.__cgpa = 'A'
        elif avg >= 60 and avg < 80 :
            self.__cgpa = 'B'
        elif avg >= 40 and avg < 60 :
            self.__cgpa = 'C'
        else :
            self.__cgpa = 'D'
        return  total, avg