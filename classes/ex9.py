class Person:
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

count_p = Person("a",10)
p1 = Person('b',12)
print(Person.counter)