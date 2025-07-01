# Create a parent class Vehicle with a method start_engine().
# Inherit it in a Car class and override start_engine() to print: "Car engine started".

class Vehicle:
    def __init__(self, VehicleName):
        self.VehicleName = VehicleName

    def start_engine(self):
        print(f"{self.VehicleName}: Engine Started")

class Start(Vehicle):
    def start_engine(self):
        print(f"{self.VehicleName}: Turbo Engine Started")

Ford = Start("FordCar")
Tesla = Start("Tesla")

Ford.start_engine()
Tesla.start_engine()