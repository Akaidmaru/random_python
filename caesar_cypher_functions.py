def caesar_cypher(string, rot):
    """Cyphers a string using given rot. Rot is a key number that helps you to cypher the letters. Remember to give the Rot to the person that will be decyphering the string."""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    string = string.lower()
    encrypted_string = ""

    for index in range(rot):
        alphabet.append(alphabet[index])

    for character in string:
        if character in alphabet:
            encrypted_string += alphabet[alphabet.index(character) + rot]
        else:
            encrypted_string += character

    return print(encrypted_string)

def caesar_decypher(string, rot):
    """Decyphers a string using given rot. Rot is a key number that helps you to decypher the letters. Remember to ask the Rot to the person that will be cyphering the string."""
    string = string.lower()
    decrypted_string = ""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for letter in string:
        if letter in alphabet:
            decrypted_string += alphabet[alphabet.index(letter) - rot]
        else:
            decrypted_string += letter

    return print(decrypted_string)

