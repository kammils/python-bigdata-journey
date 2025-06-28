# Eligible age to vote
# age = int(input("Enter the age: "))
# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are ineligible to vote")

# Grade of a students

# marks = int(input("Enter the marks: "))

# if marks >= 90:
#     print("Grade: A+")
# elif marks >= 75:
#     print("Grade: A")
# elif marks >= 60:
#     print("Grade: B")
# elif marks >= 40:
#     print("Grade: C")
# else:
#     print("Grade: Fail")

# Nested condition
# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "admin":
#     if password == "secret":
#         print("Access granted.")
#     else:
#         print("Incorrect password.")
# else:
#     print("Unknown user.")


# Write a program to: "Child" if < 13:  "Teen" if 13–19 : "Adult" if 20–59 :   "Senior" if 60+

age = int(input("Enter the age: "))

if age < 13:
    print("Child")
    if (age >= 13 & age <=19):
        print("Teen")
    if (age >= 20 & age <= 59):
        print("Adult")
else:
    print("Senior")




