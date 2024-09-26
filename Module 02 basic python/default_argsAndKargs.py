""" function a paramiter kom dile vejal kore but kokhono
paramiter essa hoile diteo pari abr nao pari emon situation
a porle oi paramiter a 0 assign kore dile r vejal kore na """

# def sum(num1,num2,num3):
#     result = num1 + num2 + num3
#     return result

# total = sum(12,13)
# print(total)        #vejal korbe


# def sum(num1,num2,num3):
#     result = num1 + num2
#     return result

# total = sum(12,13)
# print(total)        #vejal korbe


# def sum(num1,num2,num3=0):
#     result = num1 + num2
#     return result

# total = sum(12,13)
# print(total)        #vejal korbe na ei khettere

""" bar bar new variable assign na korei args use korle ak variable
diyei sob input neowa jay ei jonno variable er samne just akta
'*' use korlei hoy eitake tuple bola hoy onekta list type er"""

""" function kono kisu return na korle compiler a none dekhay """

def all_sum(*nums):
    print(nums)

total = all_sum(25 , 34 , 123 , 81) #eikhane essa moto value dewa jay
print(total)

def all_sum(*nums):
    #print(nums)
    sum = 0
    for num in nums:
        sum=num+sum
    return sum

total = all_sum(25 , 34 , 123 , 81)
print(total)
