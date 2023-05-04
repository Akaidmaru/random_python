# Get user's name
name = input('Welcome! Please, enter your name \n>').title()

# Explanation of the program
print(f'Hello {name}!, The goal of this program is to count the total of occurrences of a letter you select that are present in a message!')

# Get user's message
sentence = input('What is the message you would like to use?\n>').lower()

# Get letter to count
letter = input('Input the letter you want to count\n>').lower()

# Count letter
letter_count = sentence.count(letter)

# Display result
print(f'The number of occurrences of the letter "{letter}" that are present in the sentence is: {letter_count}')