# python a list e array

# index =   0     1    2    3    4    5    6    7    8   eita normal indexing
numbers = [ 10 , 20 , 30 , 40 , 50 , 60 , 61 , 62 , 63 ]
# index =   -9   -8   -7   -6   -5   -4   -3   -2   -1   eita python er reverse index ulta
# 2 ta index ei kaj kora jay
print(numbers[3], numbers[-3])

# akhon akta range er moddhe sob print korte chaile list(start : end) ei structure follow korte hobe

print(numbers[1:6]) # end index er ager ghor porjonto print hobe
print(numbers[5:9])


#amr koto step por por print korbo setao implement korte pari
# ei structure a list(start:end:step)

print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[1:7:-1]) #eita faka ashbe karon step positive jaowar kotha silo
print(numbers[7:1:-1]) #eita thik ashbe karon step end theke suru korsi sei jonno negetively back asha possible
print(numbers[7:1:-3]) #eita thik ashbe karon step end theke suru korsi sei jonno negetively back asha possible

print(numbers[:]) # kono kisu define kore na dile suru theke shes porjonto chole jabe
print(numbers[5:]) # end define na korar jonno 2 theke suru kore sesh porjonto chole gese
print(numbers[:7]) # start define na korar jonno suru theke suru kore 7 porjonto chole gese

print(numbers[::-1]) #pison theke travers hobe mane easily revers hoye gese

""" shortcut to copy a list 'list(array[:])'
shortcut to reverse a list 'list(array[::-1])' """


#python er website theke data structure er list er built in function gula follow korte hobe