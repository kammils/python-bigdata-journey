list_users = ['srikanth', 'ravikanth', 'Bhargavi']

# Iteration on list examples
###  1. Basic for Loop
print("The Users list: 1")
print("--------------")
# print(list_users[0])
# print(list_users[1])
# print(list_users[2])

for users in list_users:
    print(f"Index {list_users.index(users)} : {users}")

# 2. Using range() with Index

print("----------------")
print("The Users list: 2")
print("--------------")
for i in range(len(list_users)):
    print(f"Index {i}: {list_users[i]}")

# 3. Using enumerate()
print("----------------")
print("The Users list: 3")
print("--------------")

for index, users in enumerate(list_users):
    print(f"Index {index}: {users}")

# 5. While Loop
i = 0
print("----------------")
print("The Users list: 4")
print("--------------")
while i < len(list_users):
    print(f"Index {i}: {list_users[i]}")
    i += 1

#  6. Iterating in Reverse
print("----------------")
print("The Users list: 5")
print("--------------")
for users in reversed(list_users):
    print(f"Index {list_users.index(users)} : {users}")


