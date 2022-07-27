"""
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars 
(5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. 
Return -1 if it can't be done.


make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
"""

def make_chocolate(small, big, goal):
	goal = goal - big*5
	total_bars = 0
	print(f"Goal o: {goal}")
	while goal == big*5 - total_bars:
		goal -= 1
		print(f"Goal: {goal}")
		total_bars += 1
		print(f"Total bars: {total_bars}")
  
	if goal == 0:
		return total_bars
	else:
		return -1

print(make_chocolate(1000, 1000000, 5000006))