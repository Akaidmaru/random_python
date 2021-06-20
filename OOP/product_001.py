class Product:
    # An underscore prefix works to indicate that something is private. But it can still be accessible.
    def __init__(self):
        self.data1 = 10
        self._data2 = 20

    def methodA(self):
        pass

    def _methodB(self):
        pass

p = Product()

print(p.data1)
p.methodA()
print(p._data2)
p._methodB()

# If i use a __ prefix, i can't call the method or parameter that's using it, python will mangle it and convert it to _ClassName__method/variable
