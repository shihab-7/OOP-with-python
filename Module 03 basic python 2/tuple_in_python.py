def num():
    return 2,3
print(num()) # auto tuple banay ney

things = 'pen','tripod','water bottle','phone','charger','web cam','sunglass'
# eita accidental tuple , auto hoye jay 

print(type(things))
print(things[0])
print(things[-2])
print(things[3:6]) # eitake slicing bole

if 'pen' in things:
    print("yes")


""" tuple r list kisuta same , tuple modify kora jay na """

for item in things:
    print(item)

# things[0] = 'ball'
# print(things) # error dibe 

print(len(things)) # tuple er item kotogula oita dekha jay

""" tuple er vitor list thakle oita change kora jabe 
but tuple modify kora jay na """

mega = ([1,2,3,4],[0,0,0])
print(mega[0]) 
mega[1][2] = 567 # onekta 2d array er moto 
print(mega)