class shop:

    #cart = [] # eita class attribute eita use korle sob data akshathe store hobe

    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] # eita instance attribute eita usekorle ak ak person er jonno akta kore alada section a store hobe


    def add_to_cart(self,item):
        self.cart.append(item)


mehjabeen = shop('meh jabeen')
mehjabeen.add_to_cart('shoes')
mehjabeen.add_to_cart('phone')

print(mehjabeen.cart)

nisho = shop('nisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')

print(nisho.cart)