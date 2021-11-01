# one time anonymous function (think JS)
# tradeoff
# makes code small but less readable

from functools import reduce
my_list = [1, 2, 3]

# lambda param: action(param) automatically return


print(list(map(lambda item:  item*2, my_list)))


print(list(filter(lambda item:  item % 2 == 1, my_list)))


print(reduce(lambda acc, item:  acc + item, my_list))
