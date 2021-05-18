alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt(cleartext):
	cyphertext = ""
	for char in cleartext:
		if char in alpha:
			new_pos = (alpha.find(char) + 13) % 26
			cyphertext += alpha[new_pos]
		else:
			cyphertext += char
	return cyphertext

cleartext = input("Input the text you want to cypher: ")
cleartext = cleartext.lower()
print(encrypt(cleartext))