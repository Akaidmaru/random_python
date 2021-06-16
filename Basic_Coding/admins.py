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

class Privileges():
	"""Represents the privileges you have!"""

	def __init__(self):
		self.privileges = ["Can add posts", "Can delete posts",
		"Can Kick User", "Can Ban Users", "Can mute Users"]

	
	def show_privileges(self):
		"""
		Shows which privileges has an Admin.
		"""
		print("As an Admin, you have the following privileges:")
		for i in self.privileges:
			print("- " + i)


class Admin(User):
	"""Represents an Admin"""
	def __init__(self, first_name, last_name, age, weight, height):
		"""
		Initalizes  father attributes.
		So child attributes.
		"""
		super().__init__(first_name, last_name, age, weight,
		height)
		self.privileges = Privileges()


prueba = Admin("Reddmar", "Quevedo", 29, 95, 1.80)
prueba.privileges.show_privileges()