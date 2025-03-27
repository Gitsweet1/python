class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, j_title):
        super().__init__(name, age)
        if j_title != "":
            self.jt = j_title
        else:
            self.jt = "Not work"

p1 = Person("Arik", 36)
e1 = Employee("Arie", 28, "Doctor")
print(p1.name, p1.age)
print(e1.name, e1.age, e1.jt)