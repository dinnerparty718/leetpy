from itertools import combinations
s = 'abcde'

# generate all substring (n * (n + 1)) / 2


# generate n length substring
# def subString(s, n):
#     # starting poinit
#     for i in range(len(s)-n + 1):
#         print(s[i:i + n])

# easier to come up option 1 outer loop control is lengthh of the substring, from 1 to length of the string (or not)
for n in range(1, len(s)):
    for i in range(len(s)-n + 1):
        # print(s[i:i+n])
        pass


# optiion 2 outer loop in the starting character
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        # print(s[i:j])
        pass

l = [1, 2, 3, 4]


res = []


# for n in range(1, len(l) + 1):
#     res.extend(combinations(l, n))

# print(res)

# print(list(combinations(l, 3)))


res = [s[x:y] for x, y in combinations(
    range(len(s) + 1), r=2)]


print(res)

# generate start and end
l = combinations(range(len(s) + 1), 2)

print(list(l))


print(range(len(s) + 1))
