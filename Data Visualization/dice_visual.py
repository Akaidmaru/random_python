import pygal
from die import Die

# Create 2 D6.append()
die_1 = Die()
die_2 = Die()

# make some rolls, and store results in a list.

results = [die_1.roll() + die_2.roll() for roll_num in range(1001)]

print(results)

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

"""for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
"""

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = [i for i in range(2, 13)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual_2die.svg')


squares = [i * i for i in range(10)]
"""for i in range(10):
    squares.append(i * i)"""

