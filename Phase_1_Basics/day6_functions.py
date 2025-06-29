# # Basic function
# def greet():
#     print("Hello, Python learner!")

# greet()

# # Function with parameters
# def add_numbers(a, b):
#     return a + b

# result = add_numbers(5, 3)
# print("Sum:", result)

# # Function with default argument
# def greet_user(name="Guest"):
#     print(f"Welcome, {name}!")

# greet_user("Vicky")
# greet_user()

# # Function returning multiple values
# def get_stats(numbers):
#     return min(numbers), max(numbers), sum(numbers)

# my_list = [2, 5, 7, 1]
# minimum, maximum, total = get_stats(my_list)
# print("Min:", minimum, "Max:", maximum, "Sum:", total)
\
# # Function using keyword arguments
# def introduce(name, age, city):
#     print(f"My name is {name}, I’m {age} years old from {city}.")

# introduce(age=25, name="Vicky", city="Dallas")

# ##Write a function is_even(number) that returns True if the number is even, else False

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
print(f"The give number is Even:  {is_even(1)}")

#     Create a function fahrenheit_to_celsius(f) that converts temperature from Fahrenheit to Celsius.

def fahrenheit_to_celsius(temperture):
    return((temperture - 32) * 5/9)

print(f"The temperature is : {round(fahrenheit_to_celsius(97), 2)} celsius")














