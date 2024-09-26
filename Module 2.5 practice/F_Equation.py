number = input()

num1 , num2 = number.split()
num1 = int(num1)
num2 = int(num2)
total = 0
for i in range(0,num2+1,2):
    total += num1**i
    

sum = int(total)-1
print(sum)



# def series_sum(x, n):
#     sum_result = 0
#     power = 1
#     for i in range(0, n + 1, 2):
#         sum_result += power
#         power *= x * x
#     return sum_result

# x, n = map(int, input().split())
# z = series_sum(x, n)
# print(z - 1)
