import collections
from sortedcontainers import SortedDict, SortedList, SortedSet
# list append() pop() pop(0)
# set add() remove() discard()
# dict d['key']   del d['key']   d.pop(key)

# https://www.youtube.com/watch?v=7z2Ki44Vs4E

# dict

d = SortedDict({2: 2, 9: 9, 1: 1, 3: 3})
d.get(3)

print('sorted dict')


d.setdefault(4, [])


d[4].append(4)


# delete a key
del d[4]

# give a default wont raise key error
a = d.pop(4, [])


# delete key
# del d[4]


print(d)

# remove last one
d.popitem()

print(d)
print('\nsorted set')

# set
sorted_set = SortedSet([1, 1, 1, 12, 34])
sorted_set.add(2)


sorted_set.remove(1)  # remove non eixist element will raise error
sorted_set.discard(3)

print(sorted_set)


# list


print('\nsorted list')

sorted_list = SortedList([4, 3, 2, 7, 8, 8])
print(sorted_list)


print(sorted_list.discard(8))
print(sorted_list)
