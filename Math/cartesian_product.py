
A = {'a', 'b', 'c', 'd'}  # 4 * 4 combinations


l = []

for c1 in A:
    for c2 in A:
        l.append(c1+c2)


print(l)
