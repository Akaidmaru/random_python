name = "anita.lava.la.tina"


if name.strip(".") == name[::-1]:
    print("It is a Palindrome")
else:
    print("Not a Palindrome")





# enumarate

frutas = ["manzana", "banana", "manzana", "naranja", "banana"]

for counter, fruta in enumerate(frutas, start=1):
    print(f"{counter}) {fruta}")

# 0 manzana, 1 banana, 2 manzana, 3 naranja
