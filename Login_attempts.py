class User():

	def __init__(self, first_name, last_name, age, weight,
	 height):
		"""Initializes attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.weight = weight
		self.height = height
		self.login_attempts = 0
	
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

	def increment_login_attempts(self):
		"""Updates login attempts."""
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

redd = User("Reddmar", "Quevedo", 29, 95, 1.82)

redd.increment_login_attempts() # 1
redd.increment_login_attempts() # 2
redd.increment_login_attempts() # 3
redd.increment_login_attempts() # 4
redd.increment_login_attempts() # 5
redd.increment_login_attempts() # 6

print(redd.login_attempts)

redd.reset_login_attempts()

print(redd.login_attempts)