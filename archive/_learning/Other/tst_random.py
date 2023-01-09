import random

# random number between 0 ,1
print(random.random())


# random int between [start ,end]
# 0 or 1
print(random.randint(0, 1))

# make a choice
print(random.choice(['a', 'b', 'c']))


my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)

print(my_list)
