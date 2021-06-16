# Random guess game.

import random

print("Hello! What's your name?")
name= input()

print("Well, " + name + ",  i am thinking of a number between 1 and 20")

secretNumber = random.randint(1, 20)

for attempts in range(1, 7):
	print("Give me a guess!")
	guess = int(input())

	if guess < secretNumber:
		print("Guess is too low!")
	elif guess > secretNumber:
		print("Guess is too high!")
	else:
		break # When correct, break for loop.


if guess == secretNumber:
	print("There you go!, it took you " + str(attempts) + 
		" attempts to guess it!")
else:
	print("Nope, the number i was thinking was " + str(secretNumber) +
		". You ran off of attempts! Better luck next time!")