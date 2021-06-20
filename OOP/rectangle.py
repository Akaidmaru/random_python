class Rectangle():
    def __init__(self, lenght, breadth):
        self.lenght = lenght
        self.breadth =  breadth
        self.diagonal = (self.lenght * self.lenght + self.breadth * self.breadth) ** 0.5

    def area(self):
        return self.lenght * self.breadth

    def perimeter(self):
        return 2 * (self.lenght + self.breadth)