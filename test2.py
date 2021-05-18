list1 = ['r','a','c','o','o','n']
list2 = []

while list2 != list1:
	for x in list1:
		list2.append(x)

print(list2)
print('a' in list1)
print('b' in list1)

if 'b' not in list1:
	print("No hay en la lista la letra que buscas")
elif 'a' in list1:
	print("Claro que tenemos una 'A'")
