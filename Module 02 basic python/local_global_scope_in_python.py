""" python a function er vitor global variable er maan change
korte parbo na , modify korte chaile function er paramiter a pass kore dite hobe othoba 'global'
keyword variable er agey use korte hobe but just access korte chaile kono somossa hoy na
r function er vitor local variable sudhu function er vitorei access kora jay"""

balance = 3000

def buy_things(item,price):
    global balance #global define kore na dile error dito
    print(f'balance i have {balance}')
    balance = balance-price
    print(f'remain after buying {item} is : {balance}')

buy_things('sunglass',2000)