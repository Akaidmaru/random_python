import dis
def a():
  data = [1,2,3,4,5,6,7,8]
  x = data[5]
  print(x)

def b():
  data = (1,2,3,4,5,6,7,8)
  x = data(5)
  print(x)
print("----------:List:------")
dis.dis(a)
print("----------:Tuple:------")
dis.dis(b)


lista = [1, 2, 3, 4]

for contador, elemento in enumerate(lista):
  print(f'Soy un contador: {contador}, y yo soy el elemento: {elemento}')

print(f'{"-"*30} Prueba')