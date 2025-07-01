# simpleUser = [{"Name": "Srikanth", "Age" : 37, "Country": "INDIA"},
#               {"Name": "Ravikangth", "Age" : 35, "Country": "CANADA"},
#                {"Name": "Bhargavi", "Age" : 30, "Country": "USA"} ]

# print("------------Users List--------------")
# for users in simpleUser:
#     for key in users:
#         print(f"{key}: {users[key]}")
#     print('################################')


simpleUser = [{"Name": "Srikanth", "Age" : 37, "Countries_Travelled": ['USA', 'JAPAN', 'INDIA', 'CANADA', 'AUSTRALIA']},
              {"Name": "Ravikangth", "Age" : 35, "Countries_Travelled": ['USA', 'INDIA', 'CANADA']},
               {"Name": "Bhargavi", "Age" : 30, "Countries_Travelled": ['USA', 'JAPAN']} ]


print("------------Users Travel List--------------")
for user in simpleUser:
    name = user["Name"]
    age = user["Age"]
    countries_count = len(user["Countries_Travelled"])
    print(f"Name: {name}, Age: {age}, Countries_Travelled_count: {countries_count}")


