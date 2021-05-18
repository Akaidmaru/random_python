def diff21(n):
	if n > 21:
		c = 2*(abs(21 - n))
		return c
	else:
		c = abs(21 - n)
		return c
print(diff21(21))