def array_front9(nums):
  # First figure the end for the loop
  end = len(nums)
  if end > 4:
    end = 4
  
  for i in range(end):  # loop over index [0, 1, 2, 3]
    if nums[i] == 9:
      return True
  return False
print(array_front9([1, 2, 3]))
print(array_front9([5, 5]))
print(array_front9([2]))
print(array_front9([1, 2, 3]))