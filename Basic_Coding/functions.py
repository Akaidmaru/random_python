def greet_user0():
	"""Enseña un mensaje simple de saludo al usuario."""
	print("Holi")
def greet_user1(username):
	"""Enseña un mensaje simple de saludo al usuario."""
	print("Holi " + username.title() + ", ¿Cómo estás?")
def describir_mascota(nombre_mascota, tipo_animal='perro'):
	"""Muestra informacion sobre una mascota"""
	print("Tengo un " + tipo_animal + ".")
	print("Mi " + tipo_animal.title() + " se llama: " + 
		nombre_mascota.title() + ".")
def describir_mascota2(tipo_animal, nombre_mascota):
	"""Muestra informacion sobre una mascota"""
	print("Tengo un " + tipo_animal + ".")
	print("Mi " + tipo_animal.title() + " se llama: " + 
		nombre_mascota.title() + ".")
def nombre_formateado(nombre, apellido):
	"""Regresa un nombre completo, bien formateado"""
	nombre_completo = nombre + " " + apellido
	return nombre_completo.title()
def nombre_formateado2(nombre, apellido, segundo_nombre=''):
	"""
	Regresa un nombre completo, bien formateado, recordando que el 
	segundo nombre, siempre ira de ultimo si es que se desea usar.
	"""
	if segundo_nombre:
		nombre_completo = nombre + " " + segundo_nombre+ " " + apellido
	else:
		nombre_completo = nombre + " " + apellido
	return nombre_completo.title()
def crear_persona(nombre, apellido, edad=''):
	"""Regresa un diccionario de informacion sobre una persona."""
	persona = {'Nombre': nombre, 'Apellido': apellido}
	if edad:
		persona['Edad'] = edad
	return persona 
def par(numero):
	if numero % 2 == 0:
		print("Le velda")
	else:
		return "La mentila"
def nombre_formateado3(nombre, apellido):
	"""
	Regresa un nombre completo, bien formateado
	"""
	nombre_completo = nombre + " " + apellido
	return nombre_completo.title()

while True:
	print("\nPor favor, dime tu nombre:")
	print("(Ingresa 'q' para salir.)")

	nombre = input("Nombre: ")
	if nombre.lower() == 'q':
		break

	apellido = input("Apellido: ")
	if apellido.lower() == 'q':
		break

	final_name = nombre_formateado3(nombre, apellido)
	print("Hola, " + final_name + '!')