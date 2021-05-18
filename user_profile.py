def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

def car(manufacturer, model, **misc):
	"""Builds a dictionary containing car info."""
	car_info = {}
	car_info['manufacturer'] = manufacturer
	car_info['model'] = model
	for key, value in misc.items():
		car_info[key] = value
	return car_info

x = car('honda', 'civic', VIN = 'None', color = 'red')

print(x)