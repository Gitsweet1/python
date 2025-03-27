class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi, I'm printed from class function\nName:",self.name,"\nAge:",self.age)

person1 = Person("Arik", 36)
print("Our first customer is:",person1.name)
print("His age is:",person1.age)
person1.greet()