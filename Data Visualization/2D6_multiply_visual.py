import pygal
from die import Die

# Create two D6

die_1 = Die()
die_2 = Die()

# Make some rolls and store results in a list, this time, multiplying them.

results = [die_1.roll() * die_2.roll() for roll_num in range(1001)]

print(results)

# Analyze results. 
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

hist = pygal.Bar()

hist.title = "Results of multiplying two D6 dice 1000 times."
hist.x_labels = [i for i in range(1, max_result+1)]
hist.x_title = "Result."
hist.y_title = "Frequency of Result."

hist.add('D6 * D6', frequencies)
hist.render_to_file('die_visual_2D6_Multiplication.svg')