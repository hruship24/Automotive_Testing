class StuPers:
    def __init__(self, rno, name, dept, sem):
        self._rno = rno
        self._name = name
        self._dept = dept
        self._sem = sem
        self._year = 0

    def calculate_year(self):
        if self._sem == 1 or self._sem == 2 :
            self._year = 1
        elif self._sem == 3 or self._sem == 4 :
            self._year = 2
        elif self._sem == 5 or self._sem == 6 :
            self._year = 3
        elif self._sem == 7 or self._sem == 8 :
            self._year = 4

    @property
    def name(self):
        return self._name

    @property
    def rno(self):
        return self._rno

    @property
    def dept(self):
        return self._dept

    @property
    def sem(self):
        return self._sem

    @property
    def year(self):
        return self._year
