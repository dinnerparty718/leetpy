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
