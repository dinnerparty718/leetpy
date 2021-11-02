'''
function is first class citizen like js
funciton stores in heap

make decorator possible


what is Higher Order Fucntion (HOC)
    1. a function that accespt function as param
    2. a fun tion returns a function

'''


def hello():
    print('hello')


greet = hello


del hello  # delete name reference

greet()

# not define
# hello()

# higer order function 1


def hello(func):
    func()


def greet():
    print('still here')


# pass in the function
hello(greet)


# higer order function 2

def greet2():
    return lambda x: x * 2


a = greet2()
print(a(2))
