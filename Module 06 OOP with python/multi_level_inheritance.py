class Gadges:
    def __init__(self, brand, price, color, origin) -> None:
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
    
class Phone(Gadges):
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)

    def phone_call(self, number, text):
        return f'sending sms to : {number} with : {text}'

    def __repr__(self) -> str:
        return f'phone : {self.brand} {self.price} {self.dual_sim}'

class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lense(self):
        pass



#inheritance
my_phone = Phone('iphone', 120000, 'silver', 'china', True)
print(my_phone.brand)


class BaseClass:
    pass

# derived class or child class
class DerivedClass(BaseClass):
    pass

""" 
1. simple inheritance : parent class --> child class(Gadget---> Phone) (Gadgets ---> Laptop)

2. Multi-level inheritance : Grand --> parent ---> child(vehicle--->Bus--->ACBus)

3. Multiple inheritance : Student (Family, School, Sports)

4. Hybrid inheritance : Grand--> Father,Uncle,Aunty--->Child(Father, Uncle)

 """

class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name 
        self.price = price

    def move(self):
        pass

    def __repr__(self) -> str:
        return f'{self.name} {self.price}'

class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)
    def __repr__(self) -> str:
        return super().__repr__()

class Truck(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight = weight
        super().__init__(name, price)

class PickUPTrack(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class ACBus(Bus):
    def __init__(self, name, price, seat, temperature) -> None:
        self.temperature = temperature
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f'{self.seat}')
        return super().__repr__()
    

green_line = ACBus('green', 5000000, 22, 16)
print(green_line)