# My solution
def array_diff(a, b):
    for i in b:
        if i in a:
            for j in range(a.count(i)):
                a.remove(i)
    return a

print(array_diff([1 ,2 ,2], [2]))

# Shortest solution
def array_diff(a, b):
    return [x for x in a if x not in b] # 2nd shortest.

# Other solutions
def array_diff(a, b):
    return [x for x in a if x not in set(b)] # This is the shortest time possible of execution

def array_diff(a, b):
    set_b = set(b)
    return [i for i in a if i not in set_b]

def array_diff(a, b):
    return filter(lambda i: i not in b, a)

def array_diff(a, b):
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a

def array_diff(a, b):
    for n in b:
        while(n in a):
            a.remove(n)
    return a


def array_diff(a, b):
    c = []

    for e in a:
        for e2 in b:
            if e == e2:
                break
        else:
            c.append(e)

    return c


def array_diff(a, b):
    new_list = []
    for val in a:
        if val not in b:
            new_list.append(val)

    return new_list


def array_diff(a, b):
    for x in b:
        while a.count(x) != 0:
            a.remove(x)
    return a


def array_diff(a, b):
    for el in b:
    while el in a:
        a.remove(el)
    return a

