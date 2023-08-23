# Eliminar Palabras Duplicadas:
# Dada una oración, utiliza .split() para dividirla en palabras, elimina las palabras duplicadas y luego únelas nuevamente con .join()

string = "mi mama mi me mi mima mi mama"
string_list = string.split()
parsed_list = []

for word in string_list:
    if word in parsed_list:
        continue
    else:
        parsed_list.append(word)

final = " ".join(parsed_list)

print(final)
