arroz_chino = [] 																#Lista de ingredientes para arroz chino

arroz_chino.append("Arroz")														#Acá comienzo a añadirlos
arroz_chino.append("Sal")
arroz_chino.append("Vinagre")
arroz_chino.append("Aceite")
arroz_chino.append("Ajo")
arroz_chino.append("Ajo porro")
arroz_chino.append("Chuleta ahumada")
arroz_chino.append("Tocineta")
arroz_chino.append("Frijoles")
arroz_chino.append("Pechuga de pollo")
arroz_chino.append("Jamón")
arroz_chino.append("Salsa de soya")

print("Para preparar Arroz Chino Venezonalo, la lista de ingredientes es: ")
print(arroz_chino)

print("Debemos chequear con cuáles ingredientes no contamos:")

popped1 = arroz_chino.pop(5)													#Almacenos los ingrdientes que no tengo en variables.
popped2 = arroz_chino.pop(6)
popped3 = arroz_chino.pop(6)

faltan = []																		#Lista de Ingredientes que faltan.

faltan.append(popped1)															#Añadimos las variables para crear lista.
faltan.append(popped2)
faltan.append(popped3)

print(faltan)

arroz_chino.insert(2, "Agua") 													#Se nos olvidó añadir el agua.

#print(arroz_chino)																#Línea para comprobar que tengo en la lista.

print("Para preparar el arroz, necesitamos: " + arroz_chino.pop(0) + ", " +
	arroz_chino.pop(0) + ", " + arroz_chino.pop(0)
	)

#arroz_chino.sort()																#Para ordenar alfabéticamente permanentemente.

#arroz_chino.sort(reverse=True)													Para ordenar de forma alfabética inversa.

#print(sorted(arroz_chino))														Para ordenar alfabaéticamente temporalmente.

#arroz_chino.reverse()															Orden cronológico inverso permanentemente.

print(len(arroz_chino))															#len es para saber la cantidad de elementos en la lista.