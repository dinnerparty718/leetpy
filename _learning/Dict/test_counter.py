from collections import Counter

# create a dict
li = [1, 2, 3, 4, 5, 5, 8]


sentence = 'bla bla bla python'


# print(Counter(li))
print(Counter(sentence))


# for k, v in Counter(sentence).items():
#     print(k, v)

my_counter = Counter(li)

# returns a list of tuple
common = my_counter.most_common(2)


print(common)
