"""def join_list(list1):
	return ', '.join([element for element in list1]) 
list_2 = ["H","o","l","a"]
print(join_list(list_2))

 """
"""def join_list(list1):
    return ', '.join([item.nombre for item in list1]) 

ws.cell(row=cont, column = 3).value = join_list(destinos)    
ws.cell(row=cont, column = 4).value = join_list(categorias)
ws.cell(row=cont, column = 5).value = join_list(actividades)"""


def is_square(n):    
    return 0 or n == (n ** 0.5) * (n ** 0.5)



print(is_square(300))

