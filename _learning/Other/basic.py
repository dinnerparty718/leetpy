'''

Everything is object in python
GC does not count weak ref

naming convention
snack_case
can't start variable with numbers
PI = 3.14
__ dendor method

stack and heap


file name does not collide with the standard module 
math
random


python library

pip install pandas
pip uninstall

each project need to be in it's own venv
simlar to npm package vs npm global

list packages installed in current evn

pip list



how to debug
    use linting
    use ied/editor
    read errors
    pdb -> python debugger

'''


# data type
# int float
# str
# bool    True False
# list
# tuple
# set
# dict
# None


# check type


print(f'data types')
print(type(6))
print(type(5) is int)

print(type(2*5))

print(type(2/4))

print(type(0.0001))
print(type(None))
print(type({}))
print(type(()))
print(type([]))


print("------")
a = 5
b = 2

# wrong
# c = math.floor(5/2)

c = 5 / 2


# to the power of
d = 5**b


print(d)


def function1(a) -> list:

    if a is True:
        return "True"
    else:
        return [1, 2, 3]


c = function1(False)


print(len(c))


# String Interpolation

print(f'hello word {a} {b}')


myList = [1, 2, 3]

myList.append('abc')

print(myList)


for item in myList:
    print(type(item) == int)