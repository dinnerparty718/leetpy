# tuple is immutable
print('----------------------')
print('TUPLE')

fruits = ("apple", "banana", "cherry")
a, b, c = fruits
print(a, b, c)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
green, yellow, *red = fruits
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
green, *tropic, red = fruits
print(tropic)

for item in fruits:
    print(item)
print('')

print(fruits[2])
print(len(fruits))

print('')

for i in range(len(fruits)):
    print(fruits[i])


# join tuples
t1 = ('a', 'b', 'c')
t2 = (1, 2, 3)

t3 = t1 + t2
print(t3)


# multiple tuples

t4 = t1 * 2
print(t4)


# immutable
#t1[0] = 5

# to change it, conver to list, modify and convert back

myL = list(t1)
myL[0] = 'z'

t5 = tuple(myL)
print(t5)


# count items in a tuple
print(t4.count('a'))

# get index
print(t4.index('a'))
