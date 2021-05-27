import pygal
from die import Die

# Create two D8
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.

results = [die_1.roll() + die_2.roll() for roll_num in range(1001)]

print(results)

# Analyze results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize results.
hist = pygal.Bar()

hist.title = "Results of rolling two D8 1000 times."
hist.x_labels = [i for i in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('die_visual_2d8.svg')