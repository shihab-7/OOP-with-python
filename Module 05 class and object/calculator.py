class Calculator:
    brand = 'Casio MS990'

    def add(self,num1,num2):
        print(num1+num2)
    def subs(self,num1,num2):
        print(num1-num2)
    def mult(self,num1,num2):
        print(num1*num2)
    def division(self,num1,num2):
        print(num1//num2)

result1 = Calculator()
result1.division(1,2)