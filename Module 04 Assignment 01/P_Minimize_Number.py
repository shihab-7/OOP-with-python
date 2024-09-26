num = int(input())
array = list(map(int,input().split()))

count = 0
everyEven_element = True

while everyEven_element:
    for i in range(num):
        if array[i] % 2 != 0 :
            everyEven_element = False
            break
        else :
            array[i]//=2

    if everyEven_element:
        count += 1
print(count)
