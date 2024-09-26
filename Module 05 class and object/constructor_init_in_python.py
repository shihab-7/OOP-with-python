class Phone :
    manufactured = 'chaina'

    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price


    def send_sms(self, phone, sms):
        text  = f'sending to : {phone} {sms}'
        print(text)


my_phone = Phone('subin', 'samsung', 80000)
my_phone1 = Phone('sumon', 'xiaomi', 20000)
my_phone2 = Phone('santo', 'iphone', 120000)
my_phone3 = Phone('sojib', 'poco', 40000)

print(my_phone.owner , my_phone.brand)