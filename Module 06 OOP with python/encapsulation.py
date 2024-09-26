# encapsulation --> hide details
# access modifiers : public , protected, private

""" '__' double under score diye properties private kora hoy """

class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name  #public
        self._branch = 'Banani 11'  # protected
        self.__balance = initial_deposit # private

    def deposite(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance  # function banay barire pass kore deowa jay private property
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'foinni taka nai'


rafsan = Bank('Chottto bro', 100000)
print(rafsan.holder_name)
#print(rafsan.__balance)  #eita error dibe karon class er vitor private kora asa
# class er bahire eshe access kora jabe na
print(rafsan.get_balance()) # eita error dibe na

""" public property class er bahire esheo change kore deowa jay.
protected property class er vitor ei use korte bola hoy r eta '_' single under score diye likha hoy
class er bahireo eta modify kora somvob
 """
rafsan.holder_name = 'Big bro'
print(rafsan.holder_name) # public howay change hoye gese

""" private properties o aktu system a class er bahire access kora jay 'dir()' function use kore """

rafsan.deposite(400000)
print(rafsan.get_balance())
print(rafsan.holder_name)
print(rafsan._branch)
print(dir(rafsan)) #eita use korle bujha jabe j kon key dara private property access korbo
print(rafsan._Bank__balance) # private property hower poreo access kora gelo system a  