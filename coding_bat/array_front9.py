def array_front9(nums):
	if len(nums) < 4:
		for i in nums:
			if i == 9:
				return True
		return False
	else:
		for i in nums[:4]:
			if i == 9:
				return True
		return False
print(array_front9([1, 2, 3]))
print(array_front9([5, 5]))
print(array_front9([2]))
print(array_front9([1, 2, 3]))