test = int(input())

while test > 0:
    line = input()
    line_x,line_y = line.split()
    x = int(line_x)
    y = int(line_y)
    if x < y:
        total = 0
        for num in range(x+1,y):
            if num % 2 != 0 :
                total += num
        print(total)
    else :
        total = 0
        for num in range(y+1,x):
            if num % 2 != 0:
                total += num
        print(total)
    test-=1
