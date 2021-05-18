prompt_0 = ("Escriba la unidad que desea transformar y presione Enter\n")
prompt_0 += ("Convertir de:\n1)K\n2)°C\n3)°F\n")

prompt_1 = ("\nTransformar K a: \n1)°C\n2)°F\n>")
prompt_2 = ("\nIntroduzca el valor a transformar.\n>")
prompt_3 = ("\nTransformar C a: \n1)K\n2)°F\n>")
prompt_4 = ("\nTransformar F a: \n1)°C\n2)K\n>")
prompt_5 = ("ERROR! Por favor introduzca una de las unidades o 'x' para salir")

active = True
while active:
	
	unit1 = input(prompt_0).lower()
	if unit1 == 'x':
		break

	elif unit1 == 'k':
		unit2 = input(prompt_1)
		
		if unit2 == 'c':
			value = input(prompt_2)

			if value == str:
				print("Solo aceptamos valores numéricos.")
			else:
				value = float(value)
				print((str(value - 273.15)) + "°C")

		elif unit2 == 'f':
			value = input(prompt_2)
			if type(value) == str:
				print("Solo aceptamos valores numéricos.")
			else:	
				value = float(value)
				print(str((((value - 273.15) * (9/5) + 32))) + "°F")

		elif unit2 != 'c' or unit2 !='f':
			print("por favor elija una de las unidades o 'x' para salir")
			continue	

# Condicion1 eligir la primera unidad a transformar
	elif unit1 == 'c':
		unit2 = input(prompt_3)
		
		if unit2 == 'k':
			value = int(input(prompt_2))
			if value != 0:
				print((str(value + 273.15)) + "°K")

		elif unit2 == 'f':
			value = float(input(prompt_2))
			if value != 0:
				print(str((((value * (9/5)) + 32))) + "°F")

		elif unit2 != 'k' or unit2 != 'f':
			print("por favor elija una de las unidades o 'x' para salir")
			continue

# Condicion1 eligir la primera unidad a transformar
	elif unit1 == 'f':
		unit2 = input(prompt_4)
		
		if unit2 == 'c':
			value = int(input(prompt_2))
			if value != 0:
				print((str((value - 32) * (5/9))) + "°C")

		elif unit2 == 'k':
			value = float(input(prompt_2))
			if value != 0:
				print(str((((value - 32) * (5/9)) + 273.15)) + "K")

		elif unit2 != 'k' or unit2 != 'c':
			print("por favor elija una de las unidades o 'x' para salir")
			continue
	else:
		print(prompt_5)
		




	
		
