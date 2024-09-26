numbers = [20 , 22 , 23 , 11 , 61]

odds=[]

# for num in numbers:
#     if num%2 == 1:
#         odds.append(num)

# print(odds)

for num in numbers:
    if num%2 == 1 and num%5==0:
        odds.append(num)

print(odds)

# eitai abr akline ei complex vabe kora jay

odd_and_devidable = [num for num in numbers if num%2==0 if num % 5 == 0]
print(odd_and_devidable)

# list er comprehension

players = ['tamim' , 'dhoni' , 'sakib']
ages = [35 , 40 , 29]

age_comb = []

#nested loop
for player in players:
    print('player : ',players)
    for age in ages:
        print(player, age)
        age_comb.append([player,age])
print(age_comb)

# eita chaile short a o lekha jay

age_comb2 = [[player , age] for player in players for age in ages] # [] eita use na korle tuple hoye jabe

print(age_comb2)