"""
Your task here is very special: you must design a vowel eater! Write a program that uses:

a for loop;
the concept of conditional execution (if-elif-else)
the continue statement.
Your program must:

ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to upper case
use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
print the uneaten letters to the screen, each one of them on a separate line.
"""

user_word = input("Input a word: ")

user_word = user_word.upper()
vowels = ["A", "E", "I", "O", "U"]

for letter in user_word:
    if letter in vowels:
        continue
    else:
        print(letter)
