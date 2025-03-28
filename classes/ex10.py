class School:
    students = []     

class Student:
    def __init__(self, name, age, id):
        self.student = [name, age, id]
        School.students.append(self.student)

st1 = Student("g",22,987112)
st2 = Student("figlin",21,87314)

print(School.students)