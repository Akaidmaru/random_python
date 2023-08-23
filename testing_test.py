secret_number = 45
flag = True


while flag:
    answer = int(input("You have to pick a number between 1 and 100, you have to guess it!: "))
    
    if answer == secret_number:
        print("Hey! You've won!")
        flag = False
    elif answer >= secret_number + 30 or answer <= secret_number - 30:
        print("You freezing my boy!")
    elif answer >= secret_number + 20 or answer <= secret_number - 20:
        print("You are warm")
    elif answer >= secret_number + 10 or answer <= secret_number - 10:
        print("You are hot!")
    elif answer >= secret_number + 2 or answer <= secret_number - 2:
        print("You are burning baby!")
