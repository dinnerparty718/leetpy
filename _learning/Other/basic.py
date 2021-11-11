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


import sys
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


# check variable size in memory

x = 0

print(sys.getsizeof(x))

x = 1
print(sys.getsizeof(x))

y = 1.0
print(sys.getsizeof(y))

z = True
print(sys.getsizeof(z))


# Empty
# Bytes  type        scaling notes
# 28     int + 4 bytes about every 30 powers of 2
# 37     bytes + 1 byte per additional byte
# 49     str + 1-4 per additional character(depending on max width)
# 48     tuple + 8 per additional item
# 64     list + 8 for each additional
# 224    set         5th increases to 736
# 21nd, 2272
# 85th, 8416
# 341, 32992
# 240    dict        6th increases to 368
# 22nd, 1184
# 43rd, 2280
# 86th, 4704
# 171st, 9320
# 136    func def does not include default args and other attrs
# 1056 class def no slots
# 56 class inst  has a __dict__ attr, same scaling as dict above
# 888 class def with slots
# 16     __slots__   seems to store in mutable tuple-like structure
# first slot grows to 48, and so on.
