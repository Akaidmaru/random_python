file_path = "pi_million.txt"
with open(file_path) as file_object:
	lines = file_object.readlines()

pi_string = ""

for line in lines:
	pi_string += line.rstrip()

"""print(pi_string[:52] + "...")
print(len(pi_string))"""

birthday = "020591"
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")
