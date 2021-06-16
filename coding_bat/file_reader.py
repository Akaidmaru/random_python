file_path = "C:/Users/IA/Desktop/Romeo and Juliet.txt"
"""with open(file_path) as file_object:
	contents = file_object.read()
	print(contents)"""

"""with open(file_path) as file_object:
	for line in file_object:
		print()"""

with open(file_path) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

