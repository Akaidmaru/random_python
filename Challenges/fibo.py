fib_nums = [1, 1] 
fib_nums = fib_nums + [fib_nums.append(fib_nums[i-1]+fib_nums[i-2]) for i in range(2,10)]*0
print (fib_nums)