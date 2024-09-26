# static attribute (class attribute)
# static method @staticmethod
# class method @classmethod
# differences between static and class method follow 'tutorials point'

class Shopping:
    cart = [] #class attribute or static attribute
    origin = 'china'

    def __init__(self, name, location) -> None:
        self.name = 'jamuna city'   #instance attribute
        self.location = 'jam er majhe'

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying : {item} for price : {price} and remaining : {remaining}')

    @classmethod
    def hudai_dekhi(self, item):
        print('hudai dekhi kintu kinbo na ', item)

    @staticmethod
    def multiplier(a,b):
        result = a*b
        print(result)


basundhora = Shopping('basu er dhara', 'not in a popular location')
#basundhora.purchase('lungi', 500, 1000)
#Shopping.purchase('a', 2, 3, 3)
basundhora.hudai_dekhi('lungi')
#Shopping.purchase(2, 3, 3)
Shopping.hudai_dekhi('lungi')

Shopping.multiplier(4,5) # static method instance sara use korte hoy
basundhora.multiplier(4,5) # instance diyeo use kora jay but na kora better