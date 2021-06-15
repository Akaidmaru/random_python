class Person:
    def set_details(self, name, age):
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

    def get_old(self):
        self.age = 70

p1 = Person()
p2 = Person()

p1.set_details('Reddmar', 30)
p2.set_details('Ted', 90)

p1.greet()

p2.greet()

print(p1.age)
p1.get_old()
print(p1.age)


class Test:
    pass

t1 = Test()
t2 = Test()

print(t1 == t2, end = ' ')
print(type(t1) == type(t2), end = ' ')


class Test:
    def method1(self):
        self.x = 10

    def display(self):
        self.method1()
        print(self.x)


t = Test()
t.display()


class Test:
    def method1(self, x):
        self.x = x

    def method2(self):
        self.x += 10

    def display(self):
        print(self.x)


t = Test()
t.method1(5)
t.method2()
t.display()
