def accum(s):
    final = ''
    for contador, i in enumerate(s, start=1):
        actual = i*contador
        actual = actual.title()
        if contador == 1:
            final += actual
        else:
            final += '-' + actual

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

    