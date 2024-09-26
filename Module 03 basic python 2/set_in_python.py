# list --> []
# tuple --> ()
# set --> {} , unique item's collection

numbers = [12 , 13 , 14 , 24 , 23 , 13] # list a dublicate value thakte pare
print(numbers)

num_set = set(numbers)
print(num_set) 

num_set.add(55)
print(num_set)

num_set.remove(12)
print(num_set)

# set a loop chalano jay but index a value set kora jay na

a = {1,2,3}
b = {1,2,3,4,5,6}
print(a & b)
print(a | b) #union set