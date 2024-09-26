string = input()
count_letter = 0
balanced_string = ''
string_collector = []
for letter in string:
    if letter == 'L':
        count_letter += 1
    else :
        count_letter -= 1
    
    balanced_string += letter

    if count_letter == 0:
        string_collector.append(balanced_string)
        balanced_string = ''

print(len(string_collector))
for subString in string_collector :
    print(subString)