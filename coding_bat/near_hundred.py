def near_hundred(n):
	c = abs(n - 100)
	d = abs(n - 200)

	if c <= 10 or d <= 10:
		return True
	else:
		return False

print(near_hundred(189))