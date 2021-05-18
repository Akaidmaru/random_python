"""cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

resqueted_toppings = 'mushrooms'

if resqueted_toppings != 'anchovies':
	print("NO ANCHOAS POR FAVOR")

respuesta = 42
if respuesta != 42:
	print("Esa no es la respuesta correcta")

banned_users = ['yosthon', 'francisco', 'david']
user = 'marie'

if user not in banned_users:
	print(user.title() + ", you can play Pokémon Go!")

game_active = True
can_edit = False

"""

"""
If - elif - else Statements.

if conditional_test:
	do something
"""
"""
age = 2

if age < 4:
	precio = 0
elif age >= 4 and age < 18:
	precio = 15
else:
	precio = 25

print("El coste de admision es: " + str(precio))
"""
"""
age = 64

if age < 4:
	precio = 0
elif age >= 4 and age < 18:
	precio = 15
elif age < 65:
	precio = 25 # elif = else if
elif age >= 65:
	precio = 5
print("El coste de admision es: " + str(precio))

"""
"""
users = []

if users:
	for user in users:
		if user == "Admin":
			print("Hello " + user + ", Would you like a status report?")
		else:
			print("Hello " + user + ", thanks for login in again!")
else:
	print("We need to find some users!")

"""
"""
alien_0 = {'color' : 'verde', 'puntos' : 5}
print(alien_0['color'])
print(alien_0['puntos'])
alien_0['posicion_x'] = 0
alien_0['posicion_y'] = 25

print(alien_0)

master_chief = {'salto_y' : 30, 'punos' : 5}
enemigo = {"hp" : 10, "def" : 2 }

dano_total = enemigo["hp"] - (master_chief["punos"] - enemigo["def"])

enemigo["hp"] = dano_total

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'fast', 'points' : 5}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))


del alien_0['points']

print(alien_0)

favorite_languages = {
'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'
}

for key, value in favorite_languages.items():
	print(key + " " + value)

for key in sorted(favorite_languages.keys()):
	print(key)

for value in favorite_languages.values():
	print(value)

for value in set(favorite_languages.values()):
	print(value)
"""
"""
alien_0 = {'color':'green', 'points': 5}
alien_1 = {'color':'yellow','points': 10}
alien_2 = {'color':'red','points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)
"""
"""
aliens= []


for alien_number in range(30):
	new_alien = {'color':'green', 'points': 5, 'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

for alien in aliens:
	print(alien)
"""
"""
pizza = {
	'crust': 'thick',
	'toppings': ['pepperoni', 'cheese', 'pineapple']
}

print("Tu ordenaste a " + pizza['crust'] + " pizza" +
	" con los siguientes toppings:")

for topping in pizza['toppings']:
	print("\t" + topping.title())
	"""
"""
favorite_languages = {
	'jen': ['python', 'ruby'], 
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell']
	}

for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite language(s) is/are: ")
	for language in languages:
		print("\t" + language.title())
"""

users = {
	'aeistein':
		{
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton'
		},
	'mcurie':
		{
		'first': 'marie',
		'last': 'curie',
		'location': 'paris'
		}
	}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']

	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())