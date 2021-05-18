def make_tags(tag, word):
	return "<"+ tag + ">" + word +  "</" + tag + ">"

def make_out_word(out, word):
	return out[:2] + word + out[2:4]

def extra_end(str):
	x = len(str)
	return 3 * str[x - 2:x + 1]

def extra_end(str):
  end = str[-2:]
  return end + end + end

def first_two(str):
	if len(str) < 2:
		return str
	else:
		return str[:2]

def first_half(str):
	x = int(len(str)/2)
	return str[:x]

def without_end(str):
	x = len(str)
	y = str[x - x + 1: x - 1]
	return y

def combo_string(a, b):
	if len(a) > len(b):
		return b + a + b
	else:
		return a + b + a

def non_start(a, b):
	return a[1:] + b[1:]

def left2(str):
	return str[2:] + str[:2]

def first_last6(nums): # Mine
	if nums[0] == 6 or nums[-1] == 6:
		return True
	else:
		return False

def first_last6(nums): # CodingBat
  return (nums[0]==6 or nums[-1]== 6)

def same_first_last(nums):
	return (len(nums) >= 1 and nums[0] == nums[-1])

def make_pi():
	return [3, 1, 4]

def common_end(a, b):
	return (a[0] == b[0] or a[-1] == b[-1])

def sum3(nums):
	return nums[0] + nums[1] + nums[2]

def rotate_left3(nums):
	pop0 = nums.pop(0)
	nums.append(pop0)
	return nums

"""def reverse3(nums): # First made
	pop0 = nums.pop(0)
	pop1 = nums.pop(1)
	nums.append(pop0)
	nums.append(pop1)
	return nums"""

def reverse3(nums): # Improved after investigating.
	return nums[::-1]

def max_end3(nums):
	x = max(nums[0], nums[2])
	return [x, x, x]

def sum2(nums):
	if len(nums) == 0:
		return 0
	elif len(nums) == 1:
		return nums[0]
	else:
		return nums[1] + nums[0]

def middle_way(a, b):
	return [a[1], b[1]]

def make_ends(nums):
	x = len(nums)
	return [nums[0], nums[-1]]

def has23(nums):
	if 2 in nums or 3 in nums:
		return True
	else:
		return False

def cigar_party(cigars, is_weekend):
	if is_weekend == False and cigars < 40:
		return False
	elif is_weekend == False and cigars >= 40 and cigars <= 60:
		return True
	elif is_weekend == True and  cigars < 40:
		return False
	elif is_weekend == True and cigars >= 40:
		return True
	else:
		return False

def date_fashion(you, date):
	if you <= 2 or date <= 2:
		return 0
	elif you >= 8 or date >= 8:
		return 2
	else:
		return 1

def squirrel_play(temp, is_summer):
	if is_summer == False and temp >= 60 and temp <= 90:
		return True
	elif is_summer == True and temp >= 60 and temp <= 100:
		return True
	else:
		return False

def caught_speeding(speed, is_birthday):
	if is_birthday == True:
		if speed >= 86:
			return 2
		elif speed >= 66 and speed <= 85:
			return 1
		elif speed <= 65:
			return 0
	else:
		if speed >= 81:
			return 2
		elif speed >= 61 and speed <= 80:
			return 1
		elif speed <= 60:
			return 0

def sorta_sum(a, b):
	c = a + b
	if c >= 10 and c <= 19:
		return 20
	else:
		return c

def alarm_clock(day, vacation):
	if vacation == True:
		if day >= 1 and day <= 5:
			return '10:00'
		else:
			return 'off'
	else:
		if day >= 1 and day <= 5:
			return '7:00'
		else:
			return '10:00'

def love6(a, b): # 1st Version
	if a == 6 or b == 6:
		return True
	else:
		c_sum = a + b
		c_diff = abs(a - b)
		
		if c_sum == 6 or c_diff == 6:
			return True
		else:
			return False

def love6(a, b): # Polished
	return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

def in1to10(n, outside_mode):
	if outside_mode == True:
		return n <= 1 or n >= 10
	else:
		return n >= 1 and n <= 10

def near_ten(num): # Original
	c = num % 10
	if c + 2 == 10 or c + 1 == 10 or c <= 2:
		return True
	else:
		return False

def near_ten(num): # Polished
	return num % 10 + 2 == 10 or num % 10 + 1 == 10 or num % 10 <= 2

def make_bricks(small, big, goal):
	lbricks = goal  // 5

	if lbricks > big:
		lbricks = big

	goal = goal - (lbricks * 5)

	return goal <= small

def lone_sum(a, b, c): # Mine
	if a != b and a != c and b != c:
		return a + b + c
	elif a == b and a == c and b == c:
		return 0
	elif a == b:
		return c
	elif a == c:
		return b
	elif b == c:
		return a

def lone_sum(a, b , c):
	sum = 0
	if a != b and a != c: 
		sum += a
	if b != a and b != c: 
		sum += b
	if c != a and c != b: 
		sum += c

	return sum

def lucky_sum(a, b, c):
	if a == 13: 
		return 0
	elif b == 13:
		return a
	elif c == 13:
		return a + b
	else:
		return a + b + c

def no_teen_sum(a, b, c):
	x = 0
	lista = [a, b, c]
	
	for i in lista:
		if i >= 13 and i <= 13:
			x += 0
		else:
			x += i

	return x

def fix_teen(n):
	if 