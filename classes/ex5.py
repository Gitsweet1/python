class ElectricCar:
    def __init__(self, BatteryCapacity):
        self.bc = BatteryCapacity

class GasCar:
    def __init__(self, TankCapacity):
        self.tc = TankCapacity

class HybridCar(ElectricCar, GasCar):
    def __init__(self, BatteryCapacity, TankCapacity):
        super().__init__(BatteryCapacity)
        self.bc = BatteryCapacity
        self.tc = TankCapacity

#e1 = ElectricCar(30)
#g1 = GasCar(40)
h1 = HybridCar(100,30)
print("Battery Capacity:",h1.bc)
print("Gas Capacity:",h1.tc)
