from Training.College import College


class Staff(College):
    def __init__(self, clgname, eno, name, dept):
        super().__init__(clgname)
        self._eno = eno
        self._name = name
        self._dept = dept

    @property
    def name(self):
        return self._name

    @property
    def eno(self):
        return self._eno

    @property
    def dept(self):
        return self._dept
