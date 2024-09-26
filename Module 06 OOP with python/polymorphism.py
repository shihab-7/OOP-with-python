# poly --> many/multiple
# morph --> shape

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print('Animal making sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('gheu gheu')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('maa maa')

don = Cat('real den')
don.make_sound()

shepard = Dog('kutta')
shepard.make_sound()

ruby = Goat('ruby')
ruby.make_sound()

animals = [don, shepard, ruby]
for animal in animals:
    animal.make_sound()

""" shape example """

from math import pi
class Shape:
    def __init__(self, name) -> None:
        self.name = name

class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)

    def area(self):
        return pi * self.radius * self.radius
    


circle = Circle('gol', 5)
square = Rectangle('square', 4, 4)

collection = [circle, square]
for shape in collection:
    print(shape.area())