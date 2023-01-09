numbers = [1, 2, 3, 4]


# Python reversed() method returns an iterator that accesses the given sequence in the reverse order.


for i in reversed(numbers):
    print(i)


for number in numbers[::-1]:
    print(number)

# m num of rows
# n num of colmns
m = 3
n = 2
# initialize 2d array
two_d_array = [[0] * n for _ in range(m)]

print(two_d_array)


# insert to the specified position
numbers.insert(0, 12)

print(numbers)

# split (by space)
txt = "welcome to the jungle"

x = txt.split()

print(x)

# search
sentence = 'hello'

result = sentence.index('hel')
print(result)  # 0


# You will use float('inf') and float('-inf') to represent the max and min


print(float('inf'))
print(float('-inf'))


if float('-inf') < 0:
    print('yues')


# The chr() method returns a character (a string) from an integer (represents unicode code point of
# the character).
chr(97)  # 'a'

# The ord() function returns an integer representing the Unicode character.
ord('a')  # 97


if 'a' < 'A':
    print('a < A')
else:
    print('a > A')

# unicode
# The ord() function returns an integer representing the Unicode character.
# number 48 - 57
print('0 - 9')
print(ord('0'))
print(ord('9'))


# upper case Char 65-90
print('A - Z')
print(ord('A'))
print(ord('Z'))


# upper case Char 97-122
print('a - z')
print(ord('a'))
print(ord('z'))


print()
# check if a char a alphabet or number isalnum()
print('0'.isalnum())


print('a' < 'b')  # 'a' has a smaller Unicode value


print('a' < 'A')


print("ha" * 3)


random_string = "This is a random string"


print(random_string.index('is'))
print(random_string.find('is'))
print(random_string.find('is', 9))  # if not found return -1


# print(random_string.index('is', 9))  # if not found raise exception


# find() vs index()
# find can only applify to string


print('abc'.upper())
print('ABC'.lower())


print(len('  00  '.lstrip()))  # string left
print(len('  00  '.rstrip()))  # string right
print(len('  00  '.strip()))  # string right
