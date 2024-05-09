from stud_details import Student


roll_no = int(input('Enter Roll Number : '))
name= str(input('Enter your name : '))
mo_no= int(input('Enter mobile number : '))
m1= int(input('Enter the 1st mark : '))
m2= int(input('Enter 2nd mark : '))
m3= int(input('Enter 3rd mark :'))


data = Student(roll_no, name, mo_no)
total_marks = data.total_score(m1,m2,m3)
#print(' Roll No : ',data.roll_no,'\n','Name : ', data.name ,'\n','Mobile Number : ',data.mo_no,'\n','Total mark : ',total_marks)

print(' Roll No : ',data.get_roll_no(),'\n','Total mark : ',total_marks)
data.set_roll_no(56)
print('Setting roll no : ',data.get_roll_no())

