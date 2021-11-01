# define a list
a = [1, 2, 3, 4]

# can hold different data type
a = [1, 2, 3, 4, 'Hello']

# append

a.append('appended item')

print(a)

# pop item
a.pop()


print(a)


# accessing single item
item = a[0]


# shortcut of swapping item
a[0], a[3] = a[3], a[0]

# access last item -1 is the last item
print(a[-1])


# list range end is NOT included
a = [0, 1, 2, 3, 4, 5]

print(a[1:5])
print(a[:5])
print(a[2:])


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
