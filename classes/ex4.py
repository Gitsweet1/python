class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Some sound")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def make_sound(self):
        print("Hau, Waf or Haw?")

a1 = Animal("sony", 3)
d1 = Dog("Max", 14)

a1.make_sound()
d1.make_sound()