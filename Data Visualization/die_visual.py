import pygal
from die import Die

# Create 2 D6.append()
die_1 = Die()
die_2 = Die()

# make some rolls, and store results in a list.

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

# Analyze the results.append()
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual_2die.svg')


squares = []
for i in range(10):
    squares.append(i * i)

"""
squares = [i * i for i in range(10)]
new_list = [expression for member in iterable]
new_list = [expression for member in iterable (if conditional)]

Every list comprehension in Python includes three elements:

expression is the member itself, a call to a method, or any other valid expression that returns a value. In the example above, the expression i * i is the square of the member value.
member is the object or value in the list or iterable. In the example above, the member value is i.
iterable is a list, set, sequence, generator, or any other object that can return its elements one at a time. In the example above, the iterable is range(10).
"""
