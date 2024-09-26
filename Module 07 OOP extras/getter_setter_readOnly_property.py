# read only --> you can not set the value, value can not be changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute
# setter ---> set a value of a property through a method. most of the time , you will set the value of a private property

class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money

# getter without any setter is readonly attribute 
    @property
    def age(self):
        return self._age
    # getter
    @property
    def salary(self):
        return self.__money
    
    # setter banaite chaile
    @salary.setter
    def salary(self, value):
        if value < 0:
            print('salary can not be nagetive')
        self.__money += value

samsu = User('kopa', 21, 120000)
#print(samsu.__money) # error dibe karon private property use kora jay na class er bahire 

#print(samsu.age()) # function er moto kore call kora jabe na karon decorator @property use korar jonno eta akhon attribute hoye gese
print(samsu.age) # eta kaj korbe

#print(samsu.salary()) # eita method er moto kaj kortese
print(samsu.salary)
#samsu.salary = 4500 # eita kaj korbe na karon etar jonno setter banano hoy nai

#setter bananor por kaj korbe
samsu.salary = 1000
print(samsu.salary)
