from functools import reduce
my_list = [1, 2, 3]

# map


def multipy_by2(item):
    return item * 2


print(list(map(multipy_by2, my_list)))


# filter
def check_odd(item):
    return item % 2 == 1


print(list(filter(check_odd, my_list)))


# zip


'''
    use case 
    database partition
    user name, user phone in differet table
    if they are in the same order
    zip them
'''

your_list = [10, 20, 30]
#your_list = (10, 20, 30)
their_list = ['a', 'b', 'c']

print(list(zip(my_list, your_list)))
print(list(zip(my_list, your_list, their_list)))


# reduce
# not in standard libary
'''
    aggregation
'''


def accumulator(acc, curr):
    acc += curr
    return acc


print(reduce(accumulator, my_list, 0))
