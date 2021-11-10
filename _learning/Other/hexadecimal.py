# hexadecimal 16
# 0 1 2 3 4 5 6 7 8 9 A B C D E F
# 'E7'  16 **1 * 14 + 16 ** 0 * 7
# (E7)₁₆ = (14 × 16¹) + (7 × 16⁰) = (231)₁₀


# RBG to HEX
# 0-255 0-255 0-255
# dark to white
# 256 ** 3 =  16,777,216  16.7 million combinations

# color
# (232, 125, 35) -> e8,7d,23

# FF is 256 one bytes  2 ** 8
data_bytes = bytes(b'\xFF\xFF')
print(data_bytes)


# mutable use byte array
mutable_bytes = bytearray(b'\xAD\xBE\xEE')

mutable_bytes[0] = 0
mutable_bytes.append(255)

print(mutable_bytes)

print(mutable_bytes[1:])
