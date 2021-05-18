class Car():
	"""A Simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""Initialiazes attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0


	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) +
		 " miles on it.")
	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject rolling back the odometer
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You're not allowed to roll back an odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles