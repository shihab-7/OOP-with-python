# def full_name(first , last):
#     name = f'full name is : {first} {last}'
#     return name

# """ python er function a serial maintain na korleo chole"""

# # name = full_name('alu', 'kodu')
# # print(name)
# name = full_name(last = 'kodu', first='alu') #serial maintain na korleo hoy
# print(name)

# """ key args ba kargs use kore data gula sob akta dictionary type a neowa
# jay kore akta akta kore loop use kore ba loction use kore ber
# kore ana jay . eta '**' variable er agey use kore toiri kora hoy """

# # chaile args r key args aksathe use kora jay
# # amra value fixed rekhe args ba keyargs use korte pari

# def famous_name(first , last , **addition):
#     name = f' {first} {last}'
#     print(addition['title']) #keyargs ber kora hoy eivabe
#     for key,value in addition.items():
#         print(key,value)
#     return name

# name = famous_name(first='taheri', last='ali', title='hujur', title2='shayekh', last2='taher')
# print(name)

# """ python er function a aksathe onek jinish return kora jay 
# output tuple akare dekhay but amra chaile list akareo return korte
# pari  """

# def all_get(num1,num2):
#     sum = num1 + num2
#     mul = num1 * num2
#     remain = num1 - num2
#     #return sum, mul, remain   #tuple akare
#     return [sum, mul, remain] #list akare

# everything = all_get(12,13)
# print(everything)
