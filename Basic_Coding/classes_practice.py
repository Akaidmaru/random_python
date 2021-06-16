class Restaurant():
	"""Simple Restaurant information."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initializes attributes"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Describes a restaurant"""
		print("Name: " + self.restaurant_name.title() +
		", Cuisine Type: " + self.cuisine_type.title())

	def open_restaurant(self):
		"""Displays open message."""
		print(self.restaurant_name.title() + " is now open.")

restaurant_1 = Restaurant('Reddmiamor', 'Venezuelan')
restaurant_2 = Restaurant('LeFran', 'Italian')
restaurant_3 = Restaurant('YoshNoFui', 'Peruvian')

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()


class User():

	def __init__(self, first_name, last_name, age, weight, height):
		"""Initializes attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.weight = weight
		self.height = height

	def describe_user(self):
		"""Describes user."""
		print(
			"Name: " + self.first_name.title() +
			"\nLast Name: " 	+ self.last_name.title() +
			"\nAge: " + str(self.age) +
			"\nWeight: "+ str(self.weight) + "Kg"
			"\nHeight: " + str(self.height) + "m"
			)

	def greet_user(self):
		"""Says hello to an user."""
		print("Hello " + self.first_name.title() + " " +
		self.last_name.title() +  "!")

prueba = User("Reddmar", "quevedo", 29, 95, 1.80)

prueba.describe_user()
prueba.greet_user()