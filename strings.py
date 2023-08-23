print("Hello world!")

name = "Reddmar"
last_name = "Quevedo"
age = 25
height = 1.80
weight = 90.5
total = height * weight
career = "Mechanical Engineer"
eyes = "Dark Brown"
hair = "Black"
phone_number = 918522373
boolean = True

# Classic concatenation
print(name + " " + last_name + " is " + str(age) + " years old. He is " + str(height) + " meters tall." + str(total) )

# % formatting
print("My name is %s %s and I am %s years old." % (name, last_name, age))

# Placeholders 
print("My name is {} {} and I am {} years old. I am {} meters tall.".format(name, last_name, age, height))

# F-strings
print(f"My name is {name} {last_name} and I am {age} years old. I am {height} meters tall.")

print(f"My height times my weight is {round(height * weight)} ")

print(f"My name is {name.upper()}")

print(f'{name}\'s car')

print(f"{name} is \"{age}\" years old.") 

information = ["Reddmar", "Quevedo", 32]

print(f"{information[0]} {information[1]} is {information[2]} years old.")
