def string_splosion(str):
	x = ""
	count = 1
	while count <= len(str):
		for i in str:
			x += str[:count]
			count += 1
	return x

print(string_splosion("Code"))