# 
palabra_secreta = [l, u, z]
# 
respuestas = [_,_,_]
active = True
P1 = input("Ingresa una palabra P1.")
tries = 10
while active:
	for letra in P1:
		palabra_secreta.append(letra)

	for item in palabra_secreta:
		respuestas.append("_")

	print("Ok P2, es tu turno, debes adivinar cuales letras estan en la palabra secreta.")
	print(respuestas)

	while respuestas != palabra_secreta or tries == 0:
		P2_ans = input("Ingresa la letra que crees que tiene la palabra secreta.")
		count = 0
		for letra2 in palabra_secreta:
			if P2_ans == letra2:
				print("Correcto!") 
				respuestas[count] = P2_ans
				print(respuestas)

			count += 1

	active = False