from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, width:int, height:int=None):
        self.width = width
        self.height = height if height is not None else width

    @abstractmethod
    def set_width(self, width):
        pass

    @abstractmethod
    def set_height(self, height):
        pass

    @abstractmethod
    def area(self):
        pass




class Rectangle(Shape):
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
    def area(self):
        return self.width * self.height


def test(rect):
    rect.set_width(5)
    assert rect.area() == 25
    rect.set_height(4)
    assert rect.area() == 16



square = Square(0, 0)
test(square)