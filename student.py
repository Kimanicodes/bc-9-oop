import datetime

map_ = {
    'KE': 'Kenya',
    'TZ': 'Tanzania',
    'UG': 'Uganda'
}


class Student (object):  # inheritance
    count = 0  # Initialzes Count
    class_register = {}  # Initialzises the dictionary that stores the attendance

    def __init__(self, first_name, last_name, country='KE'):
        # generate unique id
        Student.count = Student.count + 1
        self.id = Student.count
        self.first_name = first_name
        self.last_name = last_name
        self.country = map_[country]

    def attend_class(self, **kwargs):

        date = kwargs.get('date', datetime.date.today())
        loc = kwargs.get('loc', 'Hogwarts')
        teacher = kwargs.get('teacher', 'Alex')

        if date in Student.class_register.keys():
            full_name = self.first_name + " " + self.last_name
            if full_name not in Student.class_register[date]:
                Student.class_register[date].append(full_name)
        else:
            Student.class_register[date] = [
                self.first_name + " " + self.last_name]

    @staticmethod  # proposed method to print out the students who attended on a particular date
    def print_attendance(date):
        if date not in Student.class_register.keys():
            print("No Records!")
        else:
            attendance_list = Student.class_register[date]

            print("Attendance for: " + str(date))
            for student in attendance_list:
                print(student)
