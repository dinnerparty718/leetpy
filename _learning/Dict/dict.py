# key should be immutable and hashable
# list can't be key since it's mutable
# tuple can be key, tuple is mutable


d = {}


d = {"Gerge": 24, "Tom": 32}

d["YY"] = 3

if not d["YY"]:
    print('YY is not in')

print(d)
print(d.keys())
print(d.values())

for key in d:
    print(key)

# item is a tuple
for item in d.items():
    print(item)

for k, v in d.items():
    print(k, v)


# remove an key

print(d)


# remove the key and return the value
pop_item = d.pop('YY')

print(pop_item)


class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


n1 = Node(1)
n2 = Node(2)


d = {}

d[n1] = 1
d[n2] = 2


# merge dic

d1 = {'name': 'yy', 'age': 2}
d2 = {'gender': 'f'}


d3 = {**d1, **d2}

print(d3)
