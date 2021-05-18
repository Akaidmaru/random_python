def mostrar_mensaje():
	"""
	Esta función me muestra un mensaje sobre lo que hemos aprendido
	en este capítulo
	"""
	print("Estamos aprendiendo a usar funciones.")
def mi_libro_favorito(title):
	"""
	Esta funcion sirve para imprimir una frase que contenga mi libro
	favorito.
	"""
	print("Mi libro favorito es: " + title.title())
def make_shirt(size='L', msg='I Love Python'):
	print("La talla de la franela que deseas es:\n>" + size.title() +
		"\nY el mensaje que deseas es:\n>" + msg.title())
def describe_city(city_name, country= 'Japon'):
	"""
	
	"""
	print(city_name.title() + ' esta en ' + country.title())
def city_country(city='caracas', country='venezuela'):
	"""
	Funcion que regresa un par ciudad, pais.
	"""
	return city.title() + ', ' + country.title() + '.'
def make_album(artist_name,  album_title):
	'''
	Regresa un diccionario que relaciona el nombre del artista y 
	el titulo del album con la informacion ingresada.
	'''
	music_album = {	'Artista': artist_name, 'Album': album_title}
	return music_album

prompt1 = "Organizaremos tu biblioteca musical. Ingresa 'x' para"
prompt1 += " salir en cualquier momento."
active = True
resultado = 'Muchas gracias por usar mi programa, hasta luego.'

while active:
	print(prompt1)
	nombre_artista = input("Ingresa el nombre de un artista:\n>")
	if nombre_artista == 'x':
		active = False
	elif nombre_artista != 'x':
		album = input("Ingresa el titulo de un album:\n>")
		if album == 'x':
			active = False
		else:
			resultado = make_album(nombre_artista, album)
	print(resultado)
	active = False
