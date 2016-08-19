import datetime
from student import Student


s1 = Student('Yusuf', 'Hamisi')
s2 = Student('Kevin', 'Chiteri')
s3 = Student('Brian', 'Kimokoti')
s4 = Student('Arnold', 'Okoth')
s5 = Student('Beth', 'Wanjiku')
s6 = Student('Ndegwa', 'Kimani')
s7 = Student('Edison', 'Abahurire')
s8 = Student('Allan', 'Mwesigwa')
s9 = Student('Rehema', 'Wachira')
s10 = Student('Whitney', 'Ruoroh')

# Make at least 5 students attend class
s1.attend_class(loc='Hogwarts', date='18/08/2016', teacher='Alex')
s2.attend_class(loc='Hogwarts', date=datetime.date.today(), teacher='Mwale')
s3.attend_class(loc='Hogwarts', date=datetime.date.today(), teacher='')
s4.attend_class(loc='Hogwarts', date=datetime.date.today(), teacher='')
s5.attend_class(loc='Hogwarts', date=datetime.date.today(), teacher='')

# You should be able to print the list of students who
# attended class on a particular day

Student.print_attendance('18/08/2016')
