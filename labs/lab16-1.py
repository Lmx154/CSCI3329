class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def __add__(self, other):
        new_height = self.height + other.height
        new_width = self.width + other.width
        return Rectangle(new_height, new_width)

    def __str__(self):
        return f"{self.height}, {self.width}"


rect1 = Rectangle(3, 4)
rect2 = Rectangle(7, 4)

print(rect1 + rect2)
print((rect1 + rect2).area())
