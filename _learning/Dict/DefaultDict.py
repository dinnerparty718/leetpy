from collections import defaultdict
regularDict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}


# print(regularDict[4])


# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"


dDict = defaultdict(def_value)


dDict["a"] = 1
dDict["b"] = 2

print(dDict["a"])
print(dDict["b"])
print(dDict["c"])
print(dDict[""])


myDefaultD = defaultdict(lambda: 'not here', {'a': 1, 'b': 2})

a = myDefaultD['a']

print(a)


# count dict

a = 'HelloWorld'

d = {}

for c in a:
    if c not in d:
        d[c] = 0
    else:
        d[c] += 1

print(d)


# with default dict

d = defaultdict(int)

for c in a:
    d[c] += 1

print(d)
