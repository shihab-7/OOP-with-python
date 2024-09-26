person1 = {'name' : 'manik','addres' : 'dhaka', 'age' : 20, 'job' : 'student'}
# key value pair
# dictionary
# object
# hash table
# overlap with set
print(person1)
print(person1['job'])
print(person1.keys())
print(person1.values())

person1['language'] = 'python'
print(person1)
del person1['age']
print(person1)

#special dictionary looping

for key,val in person1.items():
    print(key,val)