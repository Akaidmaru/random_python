"""/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */"""

import string
import random

length = int(input("¡Vamos a generar una contraseña! Selecciona una longitud de caracteres entre 8 y 16:\n>"))

uppercase = input("¿Con o sin letras mayúsculas? 'y' para sí, 'n' para no:\n>").lower()

numbers = input("¿Con o sin números? 'y' para sí, 'n' para no:\n>").lower()

punctuations = input("¿Con o sin símbolos? 'y' para sí, 'n' para no:\n>").lower()

password = ''
parameters = ['length']

if uppercase == 'y':
    parameters.append('uppercase')

if numbers == 'y':
    parameters.append('numbers')

if punctuations == 'y':
    parameters.append('punctuations')

print(parameters)

for character in range(length):
    current_parameter = random.choice(parameters)
    
    if current_parameter == 'uppercase':
        password += random.choice(string.ascii_uppercase)
    elif current_parameter == 'numbers':
        password += random.choice(string.digits)
    elif current_parameter == 'punctuations':
        password += random.choice(string.punctuation)
    else:
        password += random.choice(string.ascii_lowercase)

print(password)
