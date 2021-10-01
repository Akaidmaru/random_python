def pyramid(n):
    return [[1]*(1+i) for i in range(n)]


print(pyramid(0))
print(pyramid(1))
print(pyramid(2))
print(pyramid(3))