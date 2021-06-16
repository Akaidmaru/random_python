from user import *

user_list =[]
prompt = "Welcome new user, let's save your information. You can type 'q' "
prompt += "to exit.\nFirst, type your username: "

while True:
    username = input(prompt)
    if username.lower() == 'q':
        break
    else:
        name = input("Enter your Name: ")
        last_name = input("Enter your Last name: ")
        password = input("Type your password: ")
        age = input("Type your age: ")
        email = input("Now your e-mail: ")
        user = User(username, name, last_name, password, age, email)
        user_list.append(user)

print("This is the registered info we have:\n")

for i in user_list:
    print(i.info())

