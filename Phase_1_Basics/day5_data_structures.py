# --- List ---
cars = ['TESLA', 'BMW', 'BENZ', 'TESLA']
print(cars)
print(f"Position of car in the list: {cars.index('BMW')}") # returns the index or position in the list of cars '1'
print(f"Rank of cars in the list: {cars.count('TESLA')}") # returns the number of occurances in the list : for cars : TESLA-2
cars.append('FERRARI') # append "FERRARI" to the list
print(f"Updated List of cars: {cars}")
cars.insert(3, "RANGE ROVER") #insert car at 3 index position in the list
print(f"New List of cars in 2025: {cars}")