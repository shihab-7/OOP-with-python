class bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000


    def get_balance(self):
        return self.balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print(f'foinni . you can\'t withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'bank fokir hoye jabe. you can\'t withdraw more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'here is your money {self.get_balance()}')


brack = bank(15000)
brack.withdraw(25)
brack.withdraw(25000000000)
brack.withdraw(2500)