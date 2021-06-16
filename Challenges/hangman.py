secret_word = "Pirata"
print("Guess the chars:")

guesses = ''
turns = 10

while turns > 0:
    attempts = 0

    guess = input("Guess a character: ")
    guesses += guess

    for char in secret_word.lower():
        if char in guesses:
            print(char)
        else:
            print("_")
            attempts += 1

    if attempts == 0:
        print("You win")

        print("The word is: ", secret_word)
        break
    

    if guess not in secret_word:

        turns -= 1

        print("Wrong!, You still have " + str(turns) + " guesses.")

        if turns == 0:
            print("Well, try again next time!")
