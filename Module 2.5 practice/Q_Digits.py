test = int (input())
while test > 0:
    number = input()
    reverse = number [::-1]
    for digit in reverse:
        print(digit,end=" ")
    print()
    test-=1