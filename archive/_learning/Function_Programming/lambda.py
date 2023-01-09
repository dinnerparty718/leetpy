# one time anonymous function (think JS)
# tradeoff
# makes code small but less readable


# A lambda cannot have a multi-line expression. This means that our expression needs to be something that can be written in a single line.

from functools import reduce
my_list = [1, 2, 3]

# lambda param: action(param) automatically return


print(list(map(lambda item:  item*2, my_list)))


print(list(filter(lambda item:  item % 2 == 1, my_list)))


print(reduce(lambda acc, item: acc + item, my_list))


print('lambda practices\n')

my_list = [5, 4, 3]

# squre
print([x**2 for x in my_list])

# list sorting
# sort base on second value asc
a = [(0, 1), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1], reverse=True)

print(a)
