class Student:
    def read_stud_data(self):
        self.r_no = int(input('Enter Roll No. : '))
        self.s_name = int(input('Enter Nane : '))
        self.addr = str(input('Enter address : '))
        self.pin_code = int(input('Enter Pine code : '))
        self.phone_no = int(input('Enter mobile No. : '))

    def disp_stud_data(self):
        print(self.r_no, self.s_name, self.addr, self.pin_code,self.phone_no)


stud = Student()
stud.read_stud_data()
stud.disp_stud_data()