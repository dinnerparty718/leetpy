'''
x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
~ x
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y 
'''


a = 5

print(bin(a))

b = int('0b101', 2)

print(b)


# floor division
# In floor division, the result is floored to the nearest smaller integer. It is also known as integer division.
c = 4 // 3
print(c)


a = 2
b = a << 1  # multiply by 2
c = a >> 1  # divide by 2

print(b, c)

a = True
b = True

c = a ^ b


print(c)

a = True
b = False

c = a ^ b

print('XOR', c)


a = False
b = False

c = a ^ b

print('XOR', c)


a = 10

print(bin(a >> 1))

print(int('101', 16))
