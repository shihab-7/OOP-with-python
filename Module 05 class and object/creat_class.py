class Phone:
    brand = 'samsung'
    color = 'black'
    price = 20000
    features = ['camere', 'speaker', 'hammer']

    def call(self): # akhon kaj korbe
        print('calling one person')

    def message(self,number,message):
        print(f'{message} from {number}')

my_phone = Phone()
print(my_phone.features)
my_phone.call() 
""" python a direct faka function
 call korle error dibe tai vitor a 'self' likhe dite hoy """
my_phone.call()
""" python er function agei default parameter self set kore niye baki parameter set korte
hobe """
my_phone.message(4444,'Call me')