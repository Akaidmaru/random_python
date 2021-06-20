class Product:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def display(self):
            print(self._x, self._y)

    @property
    def value(self):
        return self._x

    @value.setter
    def value(self, val):
        self.x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = val

p = Product(12, 24)

print(p.value)

print(p.value + 2)

p.value = 20

print(p.value)

p.y = 15

print(p.y)