"""

prompt += "\n¿Cuál es tu primer nombre?"

name = input(prompt)

print("\nHola, " + name + ", ¡Ten un lindo día!")

age = input("¿Cuántos años tienes?")

if int(age) >= 18:
	print("Eres mayor de edad")
else:
	print("Pirala menor!")

counter = 0
for i in range(1, 10):
	counter += 1
print(counter)

number = input("Ingresa un número, y te diré si es par o impar: ")
number = int(number)

if number % 2 == 0:
	print("El número " + str(number) + " es par.")
else:
	print("El número " + str(number) + " es impar.")
"""

current_number = 1

while current_number <= 5:
	print(current_number)
	current_number += 1