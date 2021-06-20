class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('I am a', self.name)

    def greet(self):
        if self.age < 80:
            print('Hello, how are you doing?')
        else:
            print('Hello, how do you do?')
        self.display()
