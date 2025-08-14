from dataclasses import dataclass

# Adaptee classes
@dataclass
class MotorCycle:
    name: str = "MotorCycle"
    def two_wheeler(self):
        return "TwoWheeler"

@dataclass
class Truck:
    name: str = "Truck"
    def eight_wheeler(self):
        return "EightWheeler"

@dataclass
class Car:
    name: str = "Car"
    def four_wheeler(self):
        return "FourWheeler"

# Adapter class
@dataclass
class VehicleAdapter:
    obj: object
    wheels: callable

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

# Main
if __name__ == "__main__":
    vehicles = [
        VehicleAdapter(MotorCycle(), wheels=MotorCycle().two_wheeler),
        VehicleAdapter(Truck(), wheels=Truck().eight_wheeler),
        VehicleAdapter(Car(), wheels=Car().four_wheeler)
    ]

    for v in vehicles:
        print(f"A {v.name} is a {v.wheels()} vehicle")
