# This creates an Alphabet List, that we would be using for this script.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Asks for an input and converts it in lowercase
input_string = input("Ingresa un string: ").lower()

# Rot is a variable to cypher the text
rot = 3

# Creates an empty string that we would be using to add letters to it
encrypted_string = ""

# "Bigger Alphabet": Using Rot variable, this would be adding the quantity of letters in the alphabet list to make it larger, this way, we avoid an out of index error
for index in range(rot):
    alphabet.append(alphabet[index])

# Works by taking each character in the input_string variable, and then, if the letter is in the alphabet list, it search its index adds rot variable and then it concatenates given index(letter) to the encrypted_string. If the character is not in the alphabet list, it would add the current character to encrypted_string variable
for character in input_string:
    if character in alphabet:
        encrypted_string += alphabet[alphabet.index(character) + rot]
    else:
        encrypted_string += character

# Prints encrypted_string variable
print(encrypted_string)

#####
# Creates an empty string
decrypted_string = ""

# This code deletes the previous letters added to the alphabet list. We need to remove them in order to work with negative indexes
for number in range(rot):
    alphabet.pop()

# IDEM as line 17, but we change the + for - because we need to revert the process of encryption. Also, we changed encrypted_string variable for decrypted_string variable.
for letter in input_string:
    if letter in alphabet:
        decrypted_string += alphabet[alphabet.index(letter) - rot]
    else:
        decrypted_string += letter

# Prints the decrypted_string
print(decrypted_string)
