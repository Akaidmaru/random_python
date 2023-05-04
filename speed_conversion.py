# Get user input value and convert it to float
speed_miles = float(input('Welcome to the Speed conversion program! Please, enter the speed in Miles per second you want to convert!\n>'))

# Conversion Ratio
conversion_ratio = 0.4474

# Display result and round it to 2 decimals
print(f'Your speed in meters per second is : {round(speed_miles * conversion_ratio, 2)}')
