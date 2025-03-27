class Car:
    def __init__(self, model="Seat"):
        self.model = model

c1 = Car()
c2 = Car("Toyota")

print(c1.model)
print(c2.model)