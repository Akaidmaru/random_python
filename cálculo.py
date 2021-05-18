porcentaje = 0.08
inversion_inicial = 3000
lista_total = []
for i in range(1, 13):
	total = inversion_inicial * porcentaje
	lista_total.append(total)
	inversion_inicial = inversion_inicial + total

print(inversion_inicial)
print(lista_total)