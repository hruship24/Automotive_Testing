from Training.College import College


class Student(College):
    def __init__(self, clgname, rno, name, dept):
        super().__init__(clgname)
        self._rno = rno
        self._name = name
        self._dept = dept

    @property
    def name(self):
        return self._name

    @property
    def rno(self):
        return self._rno

    @property
    def dept(self):
        return self._dept
