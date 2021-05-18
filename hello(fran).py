#msg_0 and msg_1 are examples of variables and strings, i can use either '' or 
#"" to create strings, also i can use \' to use single quote in a string.
msg_0 = "Hello World, we are learning Python 3, this is a good chance to start!"
msg_1 = 'How are you?'

#I created vars to test some functions inside Python,
#like concatenating strings.
name = " franCisco "
last_name = " parra trcka"
age = "26"
full_name = name + " " + last_name

print("Hello" + " " + full_name.title() + "!")

#Here i tested \n which is an enter and \t which is an indentation.
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#I used .lstrip() to remove blank space in the var.
print(last_name.lstrip())

#I used .upper(), .lower(), .title() to change everything uppercase, lowercase 
#and titlecase.
print("\n" + name.upper() + "\n" + name.lower() + "\n" + name.title())

#This is other solution to the problem.
#name_up = name.upper()
#name_lo = name.lower()
#name_ti = name.title()

#print(name_up)
#print(name_lo)
#print(name_ti)

#print(msg_0)
#this removes all blanks to both sides of a string.
#print(name.strip())