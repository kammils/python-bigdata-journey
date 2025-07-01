# Define a class with __init__
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        print(f"My name is {self.name}, I'm {self.age} years old, majoring in {self.major}.")

# Create student objects
s1 = Student("Nikhila", 23, "Data Analytics")
s2 = Student("Dharani", 25, "Big Data")

s1.introduce()
s2.introduce()
