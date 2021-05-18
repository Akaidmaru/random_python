print("How many Cats do you have?")
numCats = input(a)

try: 
	if int(numCats) >= 4:
		print("That's a lot of cats!")
	elif int(numCats) <= -1:
		print("That's impossible, i can't give you my cats!")
	else:
		print("That's not many cats!")
except ValueError:
	print("You did not enter a number")