def array123(nums):
	# First, we must create an array of [1,2, 3 ] to compare.
	seq = [1, 2, 3]
	# Then, we need a loop to compare seq to nums.
	for i in range(len(nums)):
		if seq == nums[i-1:i+2]:
			return True
	return False

print(array123([1, 1, 2, 1, 2, 3]))