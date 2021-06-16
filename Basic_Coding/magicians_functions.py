"""8-9. Magicians: Make a list of magician’s names . Pass the list to a function
called show_magicians(), which prints the name of each magician in the list ."""

magicians_names = ['fran', 'rick', 'redd', 'yosh']

def show_magicians(nombres):
	"""
	Una pequeña función que va a imprimir los nombres que estén dentro
	de una lista.
	"""
	for magician in nombres:
		print(magician.title())

"""8-10. Great Magicians: Start with a copy of your program from Exercise 8-9 .
Write a function called make_great() that modifies the list of magicians by add-
ing the phrase the Great to each magician’s name . Call show_magicians() to
see that the list has actually been modified ."""

def make_great(nombres):
	"""
	Pequeña función que va a leer una lista de nombres, lo que hará es
	leer cada elemento de una lista, le hará pop a cada elemento, 
	luego le añadirá 'the great' al final de cada elemento para luego 
	añadirlo a la misma lista, así quedará la lista original, modificada.
	"""
	for magician in nombres:
		x = nombres.pop(0)
		x += " the great"
		nombres.append(x)

"""8-11. Unchanged Magicians: Start with your work from Exercise 8-10 . Call the
function make_great() with a copy of the list of magicians’ names . Because the
original list will be unchanged, return the new list and store it in a separate list .
Call show_magicians() with each list to show that you have one list of the origi-
nal names and one list with the Great added to each magician’s name ."""

def make_great(nombres):
	for magician in nombres:
		x = nombres.pop(0)
		x += " the great"
		nombres.append(x)
	return nombres

y = make_great(magicians_names[:])
show_magicians(magicians_names)
show_magicians(y)