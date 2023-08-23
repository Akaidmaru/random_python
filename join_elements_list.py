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

# JOIN

list_2 = ["H","o","l","a"]
print("".join(list_2))

number_list = ['1', '2', '3', '4', '5']
separator = "#"
print(separator.join(number_list))


my_dict = {"name": "Alejandra", "last_name": "Leal"}
separator = "TESTING"

print(separator.join(my_dict.values()))

# SPLIT

string = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
string_2 = "Reddmar, Quevedo, Carrasquero"
string_list = string_2.split(",")

print(string_list)
