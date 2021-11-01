'''
The only difference between dict() and OrderedDict() is that:

OrderedDict preserves the order in which the keys are inserted.

Ordered Dict can be used as a stack with the help of popitem function. Try implementing LRU cache with Ordered Dict.

can be implemented with HashMap + LinkedList

'''

from collections import OrderedDict

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4


print(d)


for k, v in d.items():
    print(k, v)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)
