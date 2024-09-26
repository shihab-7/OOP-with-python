
from abc import ABC, abstractmethod
# abc ---> abstract base class

class Animal(ABC):
    @abstractmethod # enforce all derived class to have a eat method
    def eat(self):
        print('I need food ')

    
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.catagory = 'Monkey'
        self.name = name
        super().__init__()
    def eat(self):
        print('hey nana, i eat banana')


lyka = Monkey('lucy')
lyka.eat()

""" abstract vs interface difference follow 'geeks for geeks' """