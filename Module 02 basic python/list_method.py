# array te kisu last a add korte append()
numbers = [10 , 20 , 30 , 40 , 50]

numbers.append(44)

print(numbers)

#jekono position a insert korte insert(index,value)
numbers.insert(2,100)
print(numbers)

# remove korte remove(value) , akhon value jodi list a na thake tahoile error dibe eita solve korar jonno if condition use korte hobe

#numbers.remove(200)
#print(numbers) # eita error dibe

if 200 in numbers:
    numbers.remove(200)
print(numbers)  #eita error dibe na

if 10 in numbers:
    numbers.remove(10)

print(numbers)

# list er last value delete korte pop() r pop(index) dile oi index delete kore

numbers.pop() #last element delete kore
print(numbers)

numbers.pop(3) # 0 theke index count suru korle 3 no. index delete kore
print(numbers)

#kono value er index dekhte chaile index(value[,start[,end]]) use korte hobe

index = numbers.index(100) #value list a na thake -1 dibe
print(index) 

#sort korte chaile list.sort()

numbers.sort()
print(numbers)

#reverse korte chaile list.reverse()
numbers.reverse()
print (numbers)