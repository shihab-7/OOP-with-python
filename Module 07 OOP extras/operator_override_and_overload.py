class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat mangsho dim kola')

    # eita subclass a override kora na hoile error dibe
    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # eta override kora hoilo
    def eat(self):
        print('vegetables')

    def exercise(self):
        print("Push up")

#eita plus er overload
    def __add__(self, other):
        return self.age + other.age # ei function duita object plus korar jonno banaite hoy
    
#eita multiplication er overload , eivabe j kono operation korte chaile overload korte hoy
    def __mul__(self, other):
        return self.height * other.height

""" class er object gular moddhe mathemetical operation korte chaile class er vitor function banay return kore dite hobe
etakei overload kora bole , eita python er documentation theke dekhe banaite pari
"""

sakib = Cricketer('shakib', 38, 68, 91,'BD')
musfiq = Cricketer('musfiq', 36, 65, 78, 'BD')
sakib.eat()

sakib.exercise()


# (+) plus sign k overload kora hoise
print( 45 + 63 )
print( 'sakib' + 'Hasan' )
print( [1 , 2 , 3 ] + [4, 5, 6] )
print( sakib + musfiq ) 