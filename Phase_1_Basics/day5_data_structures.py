# --- List ---
# 
# cars = ['TESLA', 'BMW', 'BENZ', 'TESLA']
# print(cars)
# print(f"Position of car in the list: {cars.index('BMW')}") # returns the index or position in the list of cars '1'
# print(f"Rank of cars in the list: {cars.count('TESLA')}") # returns the number of occurances in the list : for cars : TESLA-2
# cars.append('FERRARI') # append "FERRARI" to the list
# print(f"Updated List of cars: {cars}")
# cars.insert(3, "RANGE ROVER") #insert car at 3 index position in the list
# print(f"New List of cars in 2025: {cars}")

# cars = ['TESLA', 'BMW', 'BENZ', 'TESLA2']
# Maker = ['Tesla Group', 'BMW Group', 'GE Motors']
# list = [cars, Maker]
# list[0].append('TATA')
# print(f"The list: {list[0]}")

# cars = ['TESLA', 'BMW', 'BENZ', 'TESLA']
# if 'TESLA' in cars:
#     print("Car TESLA is available")
# else:
#     print("Car is not available in the list")

# c_list = [input(" This is string1: "), input("This is string2: ")]
# print(c_list)
# t_list = []
# t_list.append('Srikanth')
# print(t_list)


# matrix = [[1,2], [3,4]]
# for i in matrix:
#     for j in i:
#         print(j)


#######################################Tuple Practise####################################

# tuple = ('Srikanth', True, 12)
# print(tuple)
# print(tuple.index(True))

# coordinates = (2, 20)
# print(coordinates[0])
# print(coordinates[1])

# set_x = {1, 2, 3, 3}
# print(set_x)

# kpairs = {"name": "ravikanth", "name": "Srikanth"}
# print(kpairs)

# # --- List ---
# fruits = ["apple", "banana", "cherry"]
# print(fruits[1])  # banana
# fruits.append("orange")
# print(fruits)
# fruits.remove("banana")
# print("After removal:", fruits)

# # --- Tuple ---
# colors = ("red", "green", "blue")
# print(colors[0])
# # colors[1] = "yellow"  # ❌ Error: Tuples are immutable

# # --- Set ---
# numbers = {1, 2, 3, 2, 1}
# print("Set:", numbers)  # Duplicates removed
# numbers.add(4)
# print("After add:", numbers)

# --- Dictionary ---
# student = {
#     "name": "Vicky",
#     "age": 25,
#     "course": "Python"
# }
# print(student["name"])
# student["age"] = 26  # update value
# print("Updated student:", student)

# # Loop through dictionary
# for key, value in student.items():
#     print(key, "=>", value)

# print(student.items())

# Write a dictionary for a book with keys: title, author, year, price.

book_store = {
    "title": 'IKIGAI',
    "author": 'Japanilo',
    "year": 2025,
    "price": 20
}

print(book_store)

for key in book_store:
    print(f"{key} : {book_store[key]}")


set_fav_programs = {'Java', 'JavaScript'}
print(set_fav_programs)
set_fav_programs.add('Python')
print(set_fav_programs)












