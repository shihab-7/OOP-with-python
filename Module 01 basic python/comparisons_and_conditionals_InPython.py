""" > , < , >= , <= , == , !== , += , -= , *= , /=
in , not , not in , is , is not """

a = 2
nibo = True
if a > 5:
    print('5 er beshi')
    print('koto beshi ?') #same indentation a likhte hobe
    # ak condition er under a akadhik kaj korte
elif a == 2 :
    print("soman soman")
else :
    print("ki silo")

if nibo is True :
    print("neo essa")
else:
    print("nio na")

if nibo is not True:
    print("nio na")
else:
    print("nio")

#nested condition
coin = 'head'

""" indentation maintain kore nested korte hoy """

toss = True 

if toss == True and coin=='head':
    print('you win')
    if 8%2==0 :
        print('go to bat')
    else :
        print('ball')
elif toss == True or coin =='head':
    print('wait a sec')
else :
    print('come tomorrow')
