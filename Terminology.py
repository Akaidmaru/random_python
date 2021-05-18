Python = 'Un lenguaje de programacion de alto nivel que puede ser usado'
Python += 'para desarrollo web, desarrollo de juegos, machine learning'
Python += 'IA, Data Science, Data Visualization, Dekstop GUI, Web'
Python += 'scrapping, aplicaciones empresariales, aplicaciones CAD'
Python += 'y aplicaciones.'

Alto_nivel = 'Dificil de entender para computadora, pero para el humano'
Alto_nivel = ' es bastante sencillo de entender. Ex.: Python'
Medio_nivel = 'Igual que el anterior, pero a un nivel medio. Ex.: C#'
Bajo_nivel = 'Opuesto al Alto_nivel. Ex.: Fortran'

string_cadenadetexto = 'Es un comentario escrito en comillas simples o'
string_cadenadetexto += ' simples, que va a ser interpretado por Python'
string_cadenadetexto += ' como un conjuto de elementos uno al lado del '
string_cadenadetexto += 'otro, pero a su vez como un todo.'

variable = 'Es un elemento que puede ser asignado o cambiado de valor'
variable += ' cada vez que se requiera, se pueden crear infinita cantidad'
variable += 'de variables, para ser usadas a lo largo del programa.'

programa = 'Es un conjunto de reglas o comandos que son dadas a la '
programa += 'computadora para que haga ciertas tareas o cumpla fun'
programa += 'ciones que sean requeridas.'

data_types = 'Strings, Integers, Floats, Booleans, None'
# int(convert_to_integer), str(converted_to_string), float(converted_to_float)

extra = 'Lists, Tuples, Dictionaries'
lists = 'Almacenan elementos y es mutable.'
tuples = 'Almacenan elementos y no es mutable.'
dictionaries = 'Almacenan elemetos, relacionas los valores con llaves,'
dictionaries += 'y tambien es mutable.'

lista1 = ['elemento1', 'elemento2', 'elemeton']
tupla1 = ('elemento1', 'elemento2', 'elemeto3', 'elemeton')
diccionario1 = {
'Key1': ['Valor1.1','Valor1.2','Valor1.1'], 
'Key2': ['Valor2.1','Valor2.1','Valor2.1'], 
'Keyn': ['ValorN.1','ValorN.2', 'ValorN.1']}

x = 'Reddmar'
y = 'Jose'
z = 'Quevedo'

# DICCIONARIO DENTRO DE UN DICCIONARIO

"""
users = {}
user = input('Marico, ingresa tu usario para almacenarlo en el sistema: ')
pw = input('Ahora guebon, ingresa tu contrasena')
users[user] = {}
users[user]['contrasena'] = pw
print(users)
"""

"""
def suma(numero1, numero2):
	total = numero1 + numero2
	return 1
print(suma(60, 30))
"""

count = 0
for i in range(1, 6):
	count += 1
print(count)

count = 0
while count <= 4:
	count += 1
print(count)
