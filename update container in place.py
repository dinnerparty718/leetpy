

my_set = {1, 2, 3}


for n in my_set:
    if n % 2 == 1:
        pass

# RuntimeError: Set changed size during iteration
#        my_set.remove(n)


# use set comprehension
# for n in {c for c in my_set}:
#     if n % 2 == 1:
#         my_set.remove(n)

# for n in iter(my_set):
#     if n % 2 == 1:
#         my_set.remove(n)


while len(my_set):
    curr = next(iter(my_set))
    my_set.remove(curr)


print(my_set)
