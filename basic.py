import math


'''

Everything is object in python
GC does not count weak ref

stack and heap


'''

# data type
# int float
# str
# bool    True False
# list
# tuple
# set
# dict


a = 5
b = 2


c = math.floor(5/2)


# to the power of
d = 5 ** b


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



a = 1


print(type(a))


