# why using generators
# generators do not hold the whold result in memory
# more readable
# range is also a generator
# yield pauses the function and return a iterable


import sys


def square_numbers(nums):
    for i in nums:
        yield(i*i)


# list comprehension
# my_nums = [x * x for x in [1, 2, 3, 4, 5]]

my_nums = square_numbers([1, 2, 3, 4, 5])


for num in my_nums:
    print(num)


# generator shorthand
my_list = [i for i in range(10000)]
print(sum(my_list))

print(sys.getsizeof(my_list), 'bytes')


my_gen = (i for i in range(10000))
print(sys.getsizeof(my_gen), 'bytes')

print(sum(my_gen))
