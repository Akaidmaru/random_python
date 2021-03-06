import pygal
from die import Die

# Create 1 D6.append()
die_1 = Die()

# make some rolls, and store results in a list.

results = [die_1.roll() for roll_num in range(1000)]

print(results)

# Analyze the results.append()
max_result = die_1.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

"""for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
"""

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = [i for i in range(1, 13)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')


squares = [i * i for i in range(10)]
"""for i in range(10):
    squares.append(i * i)"""

