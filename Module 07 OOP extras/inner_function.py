# function is a first class object

# function er vitor function banay return kora jay abr function er moddhe function o pass kore deowa jay

def double_decker():
    print('starting the double decker')
    def inner_fun():
        print('inside the inner')
        return 3000
    return inner_fun

print(double_decker()())

def do_something(work):
    print('work started')
    work()  # function hishabe parameter receive korlam
    # print(work)
    print('work ended')

#do_something('ami busy')

def coding():
    print('coding in python')

do_something(coding) # function er vitor function pass kore dilam