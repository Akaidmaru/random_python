def diff21(n):
	total = 21 - n
	
	if total <= 0:
		return -2 * total
	else:
		return total

print(diff21(22))