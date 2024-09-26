""" base class , parent class , common attribute + functionality class
derived class, child class, uncommon attribute + functionality

sob same jinish niye akta boro class banano hoy r unique unique jinish gula 
nia soto soto alada alada class bananno hoy etai inheritance
 """

class Gadges:
    def __init__(self, brand, price, color) -> None:
        self.brand = brand
        self.price = price
        self.color = color   #common inheritance

    def run(self):
        return f'Running : {self.brand}'


class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd         # uncommon
    
    def coding(self):
        return f'learning python and practicing'
    
class Phone:
    def __init__(self, dual_sim) -> None:
       
        self.dual_sim = dual_sim

    def phone_call(self, number, text):
        return f'sending sms to : {number} with : {text}'


class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lense(self):
        pass