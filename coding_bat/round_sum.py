def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    if num % 10 < 5:
        return num - (num % 10)
    else:
        return num + (10 - num % 10)

print(round_sum(6,4,4))


"""def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(num):
    mod = num % 10
    num -= mod
    if mod >= 5:
        num += 10
    return num
"""