# set


a = set()

print(a)

a.add(1)
print(a)

a.add(2)
a.add(2)

print(a)


# interrate

for x in a:
    print(x)

new_list = list(a)
print(new_list)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)


print(z)
