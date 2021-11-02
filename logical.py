'''
 this is a comment block


'''

a = 5
b = 7
c = 6

if c > a and c < b:
    print("logical and")

if c > a or c < b:
    print("logical or")


# ternary operator


a = True if 3 == 3 else False

print(a)


print('a' > 'A')

print(0 != 1)

# and or not !=


print(not False)


#  == check equality

# print(True == 1) # True
# print('' == 1)  # False
# print([] == 1)  # False
# print(10 == 10.0) # True
# print([] == [])  # True
# print([1, 2, 3] == [1, 2, 3])

# is check memory location


print([1, 2, 3] is [1, 2, 3])  # false

print([] is [])  # false two list in different location


print('test----------')

# string and number store in the same location
print('122' is '122')  # synctax warning
print(4 is 4)  # synctax warning
print(True is True)
# list, set , tuple, dict are different
# created with different memory place
print([1, 2, 3] is [1, 2, 3])


# truthy and falsey
password = '123'
username = 'johnhy'

if username and password:
    print('yes')


a = []

if a:
    print('a is not none')
else:
    print('a is none')
