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
