# jhon = 3
# mary = 2
# adam = 7

# print(f"{jhon} , {mary} , {adam}")

# total_apples = jhon + mary + adam

# print(f"Total number of apples: {total_apples}")

# print('-'*50)

# x =  -1
# x = float(x)

# y = 3*(x**3)-2*(x**2)+3*(x)-1

# print(y)

# a = 6
# b = 3

# a /= 2 * b

# print(a)

# x = float(input("Enter the value for x: "))


# y = 1/(x+1/(x+1/(x+1/x)))

# print(f'{y}')

# hour = 12
# mins = 17
# dura = 59

# # expected output 13:16

# mins = mins + dura
# hour = hour + mins // 60
# mins = mins % 60
# hour = hour % 24

# print(f"{hour}:{mins}")
# x = int(input())
# y = int(input())

# x = x // y
# y = y // x

# print(y)

# user = input("Enter your input\n>")

# if user == 'Spathiphyllum':
#     print("Spathiphyllum is the best plant ever!")
# elif user == 'spathiphyllum':
#     print("No, I want a big Spathiphyllum!")
# else:
#     print(f"Spathiphyllum! Not {user}!")

# citizen_pit = float(input("Enter your pit\n>"))
# higher_tax = 14839.02

# if citizen_pit < 0.0:
#     tax = 0.0
# elif citizen_pit < 85528:
#     tax = round(citizen_pit * 0.18 - 556.02, 0)
# else:
#     tax = round((citizen_pit - 85528) * 0.32 + higher_tax, 0)

# print(f"The tax is: {tax} thalers.")

year = 1580

if year < 1582:
    print("Not within the Gregorian calendar period.")
elif year % 4 != 0 and year % 400 != 0:
    print("Common year")
else:
    print("Leap Year")