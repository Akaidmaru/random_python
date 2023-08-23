alphabet = "abcdefghijklmnopqrstuvwxyz"

# rot_number is the key for encryption and decryption
def encrypt(input_string, rot_number):
	cypher_text = ""
	for character in input_string:
		if character in alphabet:
			new_position = (alphabet.find(character) + rot_number) % 26
			cypher_text += alphabet[new_position]
		else:
			cypher_text += character
	return cypher_text


def decrypt(encrypted_text, rot_number):
	uncypher_text = ""
	for character in encrypted_text:
		if character in alphabet:
			new_position = (alphabet.find(character) - rot_number) % 26
			uncypher_text += alphabet[new_position]
		else:
			uncypher_text += character
	return uncypher_text


input_string = input("Input the text you want to cypher: ").lower()
print(encrypt(input_string, 4))

encrypted_text = encrypt(input_string, 4)

print(decrypt(encrypted_text, 4))
