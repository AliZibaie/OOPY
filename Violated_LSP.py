class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height


def test(rect):
    rect.set_width(5)
    rect.set_height(4)
    assert rect.area() == 20


rect = Rectangle(0, 0)
test(rect)

square = Square(0, 0)
test(square)