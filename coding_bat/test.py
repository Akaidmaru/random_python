def string_match(a, b):
	# I need a counter so we know the total of times the 2 lenght
	# string matches.
	count = 0
	# Now, i need to check the strings and do the conditions.
	# I start with string a
	for i in range(len(a)):
		# I need to relate this to string.
		for j in range(len(b)):
			# Now the conditions.
			print("A:" + a[i-1:i+1])
			print("B:" + b[j-1:j+1])
			if a[i-1: i+1] == "" and b[j-1: j+1] == "":
				# Don't count
				pass				
			elif a[i-1: i+1] == b[j-1: j+1]:
				# Count 1
				count += 1
	# Here, we return count
	return count

print(string_match('aabbccdd', 'abbbxxd'))
