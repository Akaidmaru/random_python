# Manual way
def bin_to_decimal():
    bin_number = input('Input a binary number to transform to decimal\n')
    result = 0

    for number in bin_number:
        result = result * 2 + int(number)
    return result

# Python way
def bin_to_decimal2():
    binary_str = input('Enter a Binary number to convert it to Decimal:\n>')

    decimal_number = int(binary_str, 2)

    return decimal_number


print(bin_to_decimal2())
