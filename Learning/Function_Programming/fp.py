'''
Clear + understandable
easy to extend
easy to maintain
memory efficient
dry (not repeating)



Pure Fucntion

seperation with data and behavior

1. giving input
always result same output every time

2. no side effect
    do not affect outside world
    print is a side effect


'''


def multipy_by2(li):
    new_list = []
    for i in li:
        new_list.append(i*2)
    return new_list
    # return print(new_list) not a pure fuction
    # if new_list define outside of the function, not a pure function


print(multipy_by2([1, 2, 3]))


# keep data and method seperated

wizard = {
    'name': 'Merlin',
    'power': 50
}


def attck(character):
    pass
