def string_bits(str):
	x = len(str)
	y = ""
	if x == 2:
		return str[0]
	else:
		for i in range(x):
			if i % 2 == 0:
				y = y + str[i]
			else:
				pass
		return y
print(string_bits("Heeololeo"))
