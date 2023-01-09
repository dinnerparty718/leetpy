# define a list
a = [1, 2, 3, 4]

# can hold different data type
a = [1, 2, 3, 4, 'Hello']

# append

a.append('appended item')


a[0] = 'changed'

print(a)

# pop item
a.pop()


print(a)


# accessing single item
item = a[0]


# list is muttable


# shortcut of swapping item
a[0], a[3] = a[3], a[0]

# access last item -1 is the last item
print(a[-1])


# list range end is NOT included
a = [0, 1, 2, 3, 4, 5]

# list slicing, creating a new list

print(a[1:5])
print(a[:5])
print(a[2:])
print('reversing a string')
print(a[::-1])


# equivalent to js slice()
d = a[:]

b = [0, 1, 2, 3, 4, 5]


a[0] = 99

c = True if a == b else False

print(c)
print(a)
print(b)


print('')
# loop through list

for x in a:
    print(x)

print('')

for i in range(len(a)):
    print(a[i])


# list comprehension
# map() in js

a = [1, 3, 5, 7, 9, 11]

b = [x * 2 for x in a]

print(b)

c = [x**2 for x in range(1, 7)]
print(c)

d = [x**2 for x in range(6, 0, -1)]
print(d)


# sort
# it modify the original list
print('list.sort()')
a.sort()
print(a)

a.sort(reverse=True)
print(a)

# sorted() return a new list
print('sorted()')

print(sorted(a))

# .reverse()

print('reversing')
a.reverse()
print(a)


# 2D array
# useful for image reverse

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

print(matrix[0][1])

# for i in matrix:
#     for j in i:
#         print(j)


print(matrix.count([1, 2, 3]))

basket = [1, 2, 3, 4, 5]

# adding
basket.append(9)  # return type is None, not producing result
print(basket)


basket.insert(9, 'abc')  # does not error out when index out of bound
print(basket)

basket.extend((1, 3, 3, 3))

print(basket)

print(basket.count(3))


# remove() by value
# pop(), pop(-1) by index , pop return the removed value
# clear()

basket.remove(3)  # remove the first time

print(basket)

print('-----------------------')

c = [1, 2, 3, 4, 5]
c.pop()  # equivalent to c.pop(-1)

c.pop(0)  # remove the first item
print(c)

c.clear()
print(c)


# search in the list

basket = ['a', 'b', 'c', 'd', 'e']
print('serching')
# print(basket.index('2')) #raise error

print('d' in basket)

print(basket.count('0'))


# list unpacking

a, b, *c, d = [1, 2, 3, 5, 4, 5]

print(c)


emptyist = None

if(emptyist is None):
    print('here')
