class shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self , item , price , quantity):
        product = {'item' : item, 'price': price, 'quantity' : quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            #print(item)
            total += item['price'] * item['quantity']
            print('total price',total)
            if amount < total :
                print(f'please provide {total - amount} more')
            else:
                extra = amount - total
                print(f'here is your extra money and items {extra}')



sopon = shopping('sopon')
sopon.add_to_cart('alu',50,6)
sopon.add_to_cart('alu',12,24)
sopon.add_to_cart('rice',50,5)


print(sopon.cart)
sopon.checkout(600)

# home work add a remove from cart function