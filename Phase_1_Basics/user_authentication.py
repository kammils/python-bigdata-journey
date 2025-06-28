user_credentials = [{"name": "Dharru", "password": "pass1"}, {"name": "Nikhila", "password": "pass2"}]

usr_name = input("Enter name: ")
passwrd = input("Enter password: ")

# Check if user exists with matching password
for user in user_credentials:
    if usr_name == user['name'] and passwrd == user['password']:
        print(f"{usr_name}: is a Valid User with Valid Password")
        break
    else:
        print("Invalid Username or Password. Please try again.")
