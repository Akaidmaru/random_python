# Use for the questions below:
nums = [i for i in range(1, 1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."

# 1) Find all of the numbers from 1–1000 that are divisible by 8.

# Normal

for i in nums:
    if i % 8 == 0:
        print(i)
    
# Normal wit list
div_8 = []

for i in nums:
    if i % 8 == 0:
        div_8.append(i)
print(div_8)

# List Comprehension

div_8_2 = [i for i in nums if i % 8 == 0]
print(div_8_2)

# 2) Find all of the numbers from 1–1000 that have a 6 in them
# Normal with list
list_2 = []
for i in nums:
    if "6" in str(i):
        list_2.append(i)
print(list_2)

# List comprehension
list_2_2 = [i for i in nums if "6" in str(i)]
print(list_2_2)

# 3) Count the number of spaces in a string (use string above)
string = "Practice Problems to Drill List Comprehension in Your Head."
# Normal
counter = 0
for i in string:
    if i == " ":
        counter += 1
print(counter)

# List Comprehension
list_3 = len([i for i in string if i == " "])
print(list_3)

# 4) Remove all of the vowels in a string (use string above)
# Normal 
new_string = ""
for i in string:
    if i not in ["a", "e", "i", "o", "u"]:
        new_string += i
print(new_string)

list_4 = "".join([i for i in string if i not in["a", "e", "i", "o", "u"]])
print(list_4)

# 5) Find all of the words in a string that are less than 5 letters (use string above)
# Normal
words = string.split()
list_5 = []
for i in words:
    if len(i) < 5:
        list_5.append(i)
print(list_5)
# List Comprehension
words = string.split()
list_5_2 = [i for i in words if len(i) <5]
print(list_5_2)

# 6) Use a dictionary comprehension to count the length of each word in a sentence (use string above)
# Normal
words = string.split()
dictionary_1 = {}
for i in words:
    dictionary_1[i] = len(i)
print(dictionary_1)

# Dictionary Comprehension
words = string.split()
dictionary_2 = {i:len(i) for i in words} # If i use = doesn't work
print(dictionary_2)

# 7) Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
# Normal
list_7 = []
for i in nums:
    for j in range(2, 10):
        if i % j == 0:
            if i not in list_7:
                list_7.append(i)
            else:
                continue

print(list_7)

list_7_2 = [i for i in nums for j in range(2, 10) if i % j == 0]

print(list_7_2)
