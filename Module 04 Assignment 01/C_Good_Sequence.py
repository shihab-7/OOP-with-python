size = int(input())
numbers = list(map(int,input().split()))
track = {}
for number in numbers:
    if number in track :
        track[number] += 1
    else :
        track[number] = 1
result = 0
for key , val in track.items():
    if val < key :
        result += val
    elif val > key :
        result += (val - key)

print(result)