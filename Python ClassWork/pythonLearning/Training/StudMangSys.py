'''# driver   StuPers StuMarks

from Training.StudMarks import StudMarks

stud1 = StudMarks(101, 'Hruhsi', 'CSE', 4, 12,23,34)

stud1.calculate_year()
total, avg = stud1.calculate_score()

print('Details : ', stud1.name, stud1.rno, stud1.dept, stud1.sem, stud1.year)

print('Scores : ',stud1.get_mark1(),stud1.get_mark2(),stud1.get_mark3(), total, avg)
stud1.set_mark1(10101) #checking by setting a value of mark1 , if it reflects in daa or not
print('Scores : ',stud1.get_mark1(),stud1.get_mark2(),stud1.get_mark3(), total, avg)
'''

# driver StuPers StuMarks StuGrade

from Training.StuGrade import StudGrade

stud1 = StudGrade(101, 'Hrushi', 'CSE', 4, 12,23,34)
stud1.calculate_year()
total, avg = stud1.calculate_cgpa()
print('Details : ', stud1.name, stud1.rno, stud1.dept, stud1.sem, stud1.year)

print('Scores : ',stud1.get_mark1(),stud1.get_mark2(),stud1.get_mark3(), total, avg,stud1.get_cgpa())