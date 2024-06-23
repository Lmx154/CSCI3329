class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width


    def __add__(self, other):
        new_height = self.height + other.height
        new_width = self.width + other.width
        return new_height, new_width


rect1 = Rectangle(3,4)
rect2 = Rectangle(7,4)

sum = rect1 + rect2

print(sum)
