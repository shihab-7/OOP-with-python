size = int(input())
lst = list(map(int,input().split()))

if lst == lst[::-1]:
    print("YES")
else :
    print('NO')