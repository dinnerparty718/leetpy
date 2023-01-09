# 32 bit immutable

# this is of no use :)
empty_byte = bytes(4)
# b'\x00\x00\x00\x00'


# bytearray mutable

mutable_bytes = bytearray()
# bytearray(b'')


mutable_bytes = bytearray(3)
# bytearray(b'\x00\x00\x00')


mutable_bytes = bytearray(b'\xDE\xAE\xEF')
# bytearray(b'\xde\xae\xef')


mutable_bytes[0] = 0  # use int
# bytearray(b'\x00\xae\xef')


mutable_bytes.append(255)
# bytearray(b'\x00\xae\xef\xff')


mutable_bytes[0:2]
# bytearray(b'\x00\xae')


# bytes array in hex


rList = [1, 2, 3, 4, 255]  # 0-255

arr = bytearray(rList)
# bytearray(b'\x01\x02\x03\x04\xff')


a = bin(255)
# 0b11111111

print(a)


mutable_bytes = bytearray(b'\x00\x0009')


print(mutable_bytes)
