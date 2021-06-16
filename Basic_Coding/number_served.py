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

test = Restaurant("Reddmiamor", "Venezuelan")
print(test.number_served)
test.set_number_served(5)
test.increment_number_served(30)
test.increment_number_served(65)