import math
import time
def timer(fnc):
    def inner(*args, **kwargs):
        print('time started')
        start = time.time()
        fnc(*args, **kwargs)
        #print(fnc)
        print('time ended')
        end = time.time()
        print(f'total time taken : {end - start} ')
    return inner

#timer()()

@timer
def get_factorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(f'factorial of {n} is : {result}')

get_factorial(n=1200)

#timer(get_factorial)() ei vabeo decorator banano jay but function er upor @function name diye decorator bananoi beshi valo 
