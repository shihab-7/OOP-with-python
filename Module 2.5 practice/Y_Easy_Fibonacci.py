number = int(input())

fibonacci = [0,1]

if number == 1:
    print(0)
elif number == 2:
    print("0 1")
else :
    for i in range(2,number):
        series = fibonacci[-1] + fibonacci [-2]
        fibonacci.append(series)
    for num in fibonacci:
        print(num,end=" ")