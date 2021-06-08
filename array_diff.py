#def array_diff(a, b):
#    c = [i for i in a for j in b if i != j]
#    return c
def array_diff(a, b):
    c = []
    for i in a:
        if i not in j:
            c.append(i)
        elif i in b:
            continue
    return c

print(array_diff([1,2,2],[]))