import random
moves = ["r", "p", "s"]
player_wins = ["pr", "sp", "rs"]

while True:
	player_move = input("What's your move?: ")
	if player_move == 'q':
		print("See you next time!")
		break

	computer_move = random.choice(moves)

	if player_move == computer_move:
		print("Tie")
	elif player_move + computer_move in player_wins:
		print("You win!")
	else:
		print("Loser!")

# Improve by adding scores to computer and player and at the end
# show scores. Also improve the game so the pc always wins.