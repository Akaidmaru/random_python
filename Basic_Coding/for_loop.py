"""
poke = ["d1","d2","d3","d4","d5","d6","d7","d8","d9","d0"]

for pokemon in poke:
	print("It is my favorite Pokémon: " + pokemon)
"""
"""
friends = ["Francisco", "Ricardo", "César", "Yosthon"]


for friend in friends:
	print("\tÉl es mi amigo " + friend + ".\n")

print("Son burda de maricos.")
print(friend)
"""


"""
for value in range(1,6):
	print(value)

numbers = list(range(2,20,2))
print(numbers)

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#List Comprehensions

squares = [value**2 for value in range(1,11)]
print(squares)

numbers = list(range(1,21))
print(numbers)

"""
## FIBONACCI NUMBERS

"""
fib_nums = [0, 1]         
for num in range(2, 11):
	fib_nums.append(fib_nums[num-1] + fib_nums[num-2]) 
print(fib_nums)

### Excersise 1 , Ans 1.
aLsit = [100, 200, 300, 400, 500]
bLsit = []

for i in range(1, 6):
	bLsit.append(aLsit.pop(5 - i))
print(bLsit)

### Ans 2.

cLsit = []
dLsit = []
for i in range (100, 600, 100):
	cLsit.append(i)
for i in range(1,6):
	dLsit.append(cLsit.pop(5 - i))
print(dLsit)

### Ans 3.

aLsit = [100, 200, 300, 400, 500]
aLsit = aLsit[::-1]
print(aLsit)


list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = []

for i in range(0, 4):
	list3.append(list1[i] + list2[i])
print(list3)

list1 = ["Hola ", "Toma "]
list2 = ["Cariño", "Señor"]
list3 = [x + y for x in list1 for y in list2]
print(list3)

for x in list1:
	for y in list2:
		list3.append(x + y)
print(list3)
"""
# Slicing

list1 = ["Reddmar", "Francisco", "Yosthon", "Ricardo", "Emilio", "Jojo"]
"""
for i in list1[0:3]:
	print(i + ": Tiene conocimientos en Python.")

for i in list1[3:6]:
	print(i + ": Sabe hablar webonás.")
list2 = []
for i in list1[1:6]:
	list2.append(i)
print(list2)
print(list1)

for i in list1[:6]:
	print(i)

for i in list1[0:]:
	print(i)

for i in list1[::-1]:
	print(i)

print("Estos son los 3 últimos en unirse al equipo: ")
for i in list1[-3:]:
	print(i)

list2 = list1[:]

print(list1)

dimensions = (800, 600)
dimensions = (640, 480)

print(dimensions)

"""
