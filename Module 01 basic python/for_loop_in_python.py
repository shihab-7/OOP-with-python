""" array othhoba string er upor for use korte 'in' keyword use kora hoy
"""
numbers = [1,2,3,55,66,77]
for num in numbers :
    print(num)


numbers = [1,2,3,55,66,77]
sum=0
for num in numbers:
    #print(num)
    sum = sum + num
    if sum > 20:
        print("greater" ,sum)
print(sum)

# for string example

text = "i eat rice"
for char in text:
    print(char)

""" jodi normal for loop serial wise likhte chaite tahoile 'range' keyword use 
kora hoy """

""" range function a range(shuru koto theke , sesh limit , koto kore parthoko chai(optional))
range chole n-1 porjonto """

for i in range(1,10):
    print(i)


for i in range(1,10,3):
    print(i)

friends = ['naim','shanto','sofiq']
for name in friends:
    print(name)