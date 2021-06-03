"""def no_teen_sum(a, b, c):
    if a in range(13, 20):
        a = 0
    if b in range(13, 20):
        b = 0
    if c in range(13, 20):
        c = 0

    return a + b + c"""

def no_teen_sum(a, b, c):
    for value in range(13, 20):
        if value == 15 or value == 16:
            continue
        else:
            if a == value:
                a = 0
            elif b == value:
                b = 0
            elif c == value:
                c = 0 
    return a + b + c 


print(no_teen_sum(2, 1, 15))


"""def no_teen_sum(a, b, c):
    nums = (a, b, c)
    return sum(fix_teen(n) for n in nums)


def fix_teen(n):
    return 0 if n not in (15, 16) and 13 <= n <= 19 else n"""