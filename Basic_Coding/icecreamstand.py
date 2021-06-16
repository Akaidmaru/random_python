class Restaurant():
	"""Simple Restaurant information."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initializes attributes"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Describes a restaurant"""
		print("Name: " + self.restaurant_name.title() +
		", Cuisine Type: " + self.cuisine_type.title())

	def open_restaurant(self):
		"""Displays open message."""
		print(self.restaurant_name.title() + " is now open.")

	def set_number_served(self, update):
		self.number_served = update
		print("This restaurant has served: " + str(self.number_served) + 
			" guests.")

	def increment_number_served(self, update):
		self.number_served += update
		print("This restaurant has served: " + str(self.number_served) + 
			" guests on a business day!")


class IceCreamStand(Restaurant):
	"""Represents an IceCreamStand."""
	def __init__(self, restaurant_name, cuisine_type):
		"""
		Initializes attributes of parent class.
		Also specific attributes to IceCreamStand class.!
		"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = [
		"Vanilla", "Chocolate", "Strawberry", "Peanut"
		]

	def displayFlavors(self):
		"""Prints a message displaying the flavors we have!"""
		print("We have these flavors of IceCream:")
		for i in self.flavors:
			print("- " + i)

prueba = IceCreamStand("Reddmiamor", "Venezuelan")
prueba.displayFlavors()