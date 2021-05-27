import matplotlib.pyplot as plt
from die import Die

# Create a D6

die_1 = Die()

# Make rolls and store in a list.

results = [die_1.roll() for roll_num in range(7)]
print(results)

x_values = [i for i in range(1, die_1.num_sides+1)]
y_values = results

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens,
edgecolors='none', s=40)

plt.title("Rolls of a D6 die", fontsize=24)
plt.xlabel("Sides of Die.")
plt.ylabel("Frequency of Results.")


plt.tick_params(axis=both, which=major, labelsize=14)


plt.axis([1, 6, 1, 6])
plt.show()
