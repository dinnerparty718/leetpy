# list , set , dict comprehension

my_list = [char for char in 'hello']
my_list2 = [num for num in range(100)]
my_list3 = [num * 2 for num in range(100)]
my_list4 = [num ** 2 for num in range(100) if num % 2 == 0]


print(my_list4)


# set

my_set = {char for char in 'hello'}

print(my_set)


# dict

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items() if value %
           2 == 0}


my_dict2 = {num: num*2 for num in [1, 2, 3]}

print(my_dict)
print(my_dict2)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


duplicates = list(
    {x for x in [x for x in some_list if some_list.count(x) > 1]})

print(duplicates)
