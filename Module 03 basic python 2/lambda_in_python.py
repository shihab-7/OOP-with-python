# lambda

# def double(x):  # ei type er soto soto function gula ak line a lekha jay lambda use kore
#     return x*2

double = lambda num : num*2
squared = lambda num : num * num


print(squared(9))
result = double(44)
print(result)

# map

numbers = [12 , 59 , 98 , 78 , 56 , 12]
# doubled_num = map(doubled, numbers) #direct function call kore deowa jay map er vitor\

doubled_nums = map(lambda x : x*2 , numbers)

print(numbers)
print(list(doubled_nums)) # list a convert na korle vul output dibe


actors = [
    {'name' : 'sabana' , 'age' : 65},
    {'name' : 'sabnoor' , 'age' : 45},
    {'name' : 'sabila noor' , 'age' : 30},
    {'name' : 'srabonti' , 'age' : 38},
    {'name' : 'sabana' , 'age' : 65},
    {'name' : 'shaon' , 'age' : 47},
]

juniors = filter(lambda actor : actor['age'] < 40,actors)

print(list(juniors))