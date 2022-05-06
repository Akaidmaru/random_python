def wave(string):
    lista = []
    if string == None:
        return []
    else:
        lenght = len(string)
        for count, i in enumerate(string):
            i = string[count:count+1].upper()
            
            lista.append(i)
    return lista


print(wave('test'))
