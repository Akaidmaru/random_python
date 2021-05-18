"""
current_number = 1

while current_number <= 5:
	print(current_number)
	current_number += 1
"""

#parrot.py
"""
prompt = "\nDime algo, y te lo repetiré:"
prompt += "\nEscribe 'quit' para terminar el programa."
msg = ""
while msg != 'quit':
	msg = input(prompt)
	
	if msg != 'quit':
		print(msg)

prompt = "\nDime algo, y te lo repetiré:"
prompt += "\nEscribe 'quit' para terminar el programa."

active = True
while active:
	msg = input(prompt)
	
	if msg == 'quit':
		active = False
	else:
		print(msg)

prompt = "\nIngresa el nombre de una ciudad que hayas visitado"
prompt += "\n(Ingresa 'quit' cuando quieras terminar.)"

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print("Me gustaría volver ir a: " + city.title())
current_number = 0

while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)



prompt = "\nDime, ¿Cuáles toppings deseas?"
prompt += "\nPon 'quit' para salir del programa."


active = True

while active:
	topp = input(prompt)
	if topp == 'quit':
		break	
	else:
		print("\nEste topping: " + topp.title() + " será añadido a tu pizza.")


# Si una persona es menor de 3 años, entra al cine gratis. Si están entre 3 y 12
# el boleto vale $10. Si son mayores de 12 años, el boleto es $15.
# escribir un bucle en el cual se le pregunte la edad al usuario y luego uno le
# va a decir el costo del boleto.

prompt = "El costo del boleto dependerá de tu edad, por lo tanto, vamos a verif"
prompt += "icar tu edad. Puedes escribir 'quit' para salir del programa."
prompt += "\nIngresa tu edad:\n\t"

active = True

while active:
	age = input(prompt)
	if age == 'quit':
		break
	elif int(age) < 3:
		print("El costo de tu boleto es de $0. Entras Gratis c:")
	elif int(age) >= 3 and int(age) < 12:
		print("El costo de tu boleto es de $10. Nada mal.")
	else:
		print("El costo del boleto es de $15.")

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifiying user: " + current_user.title())
	confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")

for confirmed_user in confirmed_users:
	print(confirmed_user.title())

pets = ['perro', 'gato', 'perro', 'pez dorado', 'gato', 'conejo', 'gato']
print(pets)

while 'gato' in pets:
	pets.remove('gato')

print(pets)


respuestas = {}

encuesta_activa = True

while encuesta_activa:
	name = input("\n¿Cuál es tu nombre?")
	respuesta = input("¿Cuál montaña te gustaría escalar algún día?")

	respuestas[name] = respuesta

	repetir = input("¿Te gustaría que otra persona responda? (si/no)")
	if repetir == 'no':
		encuesta_activa = False
print("\n---Respuestas de la encuesta---")

for name, respuesta in respuestas.items():
	print(name + " le gustaría escalar " + respuesta + ".")




ordenes_saduchito = [
'Queso', 'pastrami', 'Aguacate', 'Carne', 'pastrami', 'Pollo', 'mortadela',
'pastrami', 'chorizo','atún', 'caraotas'
]

sanduchitos_completados = []

print("Bienvenivo a Sanduchito para el muchachito, nos hemos quedado sin "+
	"sanduchitos de Pastrami.\n")

while 'pastrami' in ordenes_saduchito:
	ordenes_saduchito.remove('pastrami')

while ordenes_saduchito:
	preparando = ordenes_saduchito.pop()
	print("Has pedido un sanduchito de " + preparando.title() + ", comenzaremos " + 
		"a prepararlo.")
	sanduchitos_completados.append(preparando)

print("\nEstos son los sanduchitos que ya están preparados:")

numero = 0

for sanduchito in sanduchitos_completados:
	numero += 1
	print("\t" + str(numero) + ") " + sanduchito.title() + ".")



respuestas = []

prompt_0 = "Estamos encuestando a las personas, para saber a que sitios les "
prompt_0 += "gustaría ir para tener sus vacaciones de ensueños.\n"
prompt_1 = "¿Dónde serían tus vacaciones de ensueño? Escribe 'Q' para salir.\n"
prompt_2 = "Gracias por su colaboración, estos son los resultados de la"
prompt_2 += " encuesta:\n"
prompt_3 = "No ha sido ingresado nada, intenta ingresar algo."

print(prompt_0)

active = True

while active:
	answer = input(prompt_1)
	
	if answer.lower() != 'q' and answer != '':
		respuestas.append(answer)
	elif answer.lower() == 'q':
		print(prompt_2)
		active = False
	elif answer == '':
		print(prompt_3)

for i in respuestas:
	print("\t" + i)

prompt_0 = "¿Quiéres que te cuente el cuento del gallo pelón?\n"
prompt_1 = "No es que sí, te pregunté:" 
prompt_2 = "No es que no, te pregunté:"
prompt_3 = "No es que "
prompt_4 = ", te pregunté:\n"
active = True

while active:
	respuesta = input(prompt_0)
	
	if respuesta.lower() == '':
		print("¡Lograste escapar de mi trolleo!")
		active = False
	elif respuesta.lower() == "si":
		print(prompt_1)
	elif respuesta.lower() == "no":
		print(prompt_2)
	elif respuesta.lower() != "si" or respuesta.lower() != "no":
		print(prompt_3 + respuesta + prompt_4)

"""