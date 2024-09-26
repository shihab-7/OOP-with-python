num1 , num2 = map(int,input().split())
count = 0
for i in range(0 , num1+1):
    for j in range(0, num1+1):
        if num2-i-j<=num1 and num2-i-j>=0:
            count+=1

print(count)