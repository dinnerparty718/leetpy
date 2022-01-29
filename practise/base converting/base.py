# binary to decimal


a = int('1010', 2)
a = int(0b1010)
a = int('0b1010', 2)
# 10

# print(a)


# oct to decimal

b = int(0o100)
b = int('100', 8)

# print(b)


# hex to decimal

c = int(0x8E)
c = int('8E', 16)


# print(c)


# int to binary
# 0b101
d = bin(5)
# print(d)


# int to oct
# 0o216
e = oct(142)
# print(e)


e = hex(12347)
# print(e)

bytes = [chr(12347 >> (i * 8) & 0xff) for i in range(4)]
bytes.reverse()


val = 12347


# most significant value in the begining
a_bytes_big = val.to_bytes(4, 'big')

print(a_bytes_big)
