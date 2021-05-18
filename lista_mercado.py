prompt1 = "Bienvenido usuario, ingrese los objetos que desea agregar"
prompt1 += " a su lista de compras. Escriba 'ya' para finalizar."
prompt2 = "\n>"
prompt3 = "Rectifica tu lista, si tienes que modificar algo, escribe "
prompt3 += "'si'. Escribe 'no' para salir.\n>"
prompt4 = "Escribe lo que quieras eliminar de tu lista, usa 'ya' para"
prompt4 += " salir.\n>"
count = 0
lista_compras = []
active = True
print(prompt1)
while active:
	ans = input(prompt2)
	if ans.lower() == 'ya':
		print("Muchas gracias y exitos!")
		active = False
	else:
		lista_compras.append(ans.title())
		print(ans.title() + ", ha sido agregado a tu lista.")

print("\nTu lista es:\n")
for i in lista_compras:
	count += 1
	print("\t" + str(count) + ".-"+ i)

"""
ans2 = input(prompt3)

if ans2.lower() == 'no':
	print("Perfecto!, estas listo para comprar.")
elif ans2.lower() == 'si':
	ans3 = input(prompt4)
	if ans3.lower() != 'ya':
		active = True
		while actve:
			ans4 
"""
