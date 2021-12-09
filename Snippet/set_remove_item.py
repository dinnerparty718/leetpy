# https://realpython.com/python-sets/#available-operators-and-methods


# a.difference(b)  -> a - b
a = set([1, 2, 3, 4])
b = set([1, 2, 3])

# check if there is common elelment
print(a.isdisjoint(b))


c = {5, 6, 7}

print(a.isdisjoint(c))

print(a & c)  # if a and c is disjoint set, result is empty set

# print(a.difference(b))

# a = a.difference(b)


a = a - b
print(a)


set_of_num = {1, 2, 11, 6, 7, 4, 5}

print('Original Set: ')
print(set_of_num)


# Remove an element with value 11 from the set
set_of_num.remove(11)

print('Set Contents After Deletion:')
print(set_of_num)


# Error key error
# ! always check if 20 exist in the set
# set_of_num.remove(20)


# ! does not raise error
set_of_num.discard(20)


# Create a set of numbers
set_of_num = {1, 2, 11, 6, 7, 4, 5, 6}
# Elements to be deleted
to_delete = [1, 2, 4, 5]


# Remove all elements of list from the set
set_of_num.difference_update(set(to_delete))
print('Modified Set Contents:')
print(set_of_num)


# subset

x = {1, 2, 3, 4, 5}

print(x.issubset(x))


print(x <= x)


# superset

x1 = {'foo', 'bar', 'baz'}
print(x1.issuperset({'foo', 'bar'}))

x2 = {'baz', 'qux', 'quux'}
print(x1 >= x2)

print(x1 >= x1)
