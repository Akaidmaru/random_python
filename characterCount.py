import pprint

message = "Testing this shit"
count = {}

for character in message.upper():
	count.setdefault(character, 0)
	count[character] = count[character] + 1

pprint.pprint(count)
# We can also use pprint.pformat(count) that way we print the result
# as a string instead of a list. We should use a variable, Ex.:
# text = pprint.pformat(count), then, print(text).  