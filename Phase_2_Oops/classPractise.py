class Car():
    cars = []
    model = []

    def __init__(self,name):
        self.cars.append(name)
    def displayCars(self):
        print(f"{self.cars}")

car = Car('Tesla')
value = car.displayCars()
