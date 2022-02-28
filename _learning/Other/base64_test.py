import base64
import sys

'''
Why use Base64 Encoding?
Base64 is a popular method to get binary data into ASCII characters
in webpage encode images in to 64 format to avoid sepearte request

The Base64 character set contains:

26 uppercase letters
26 lowercase letters
10 numbers
+ and / for new lines (some implementations may use different characters)

'''
message = "Python is fun"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)


# original size 13

# after 20

# print(len(base64_bytes))
# print(sys.getsizeof(message))


# https://stackoverflow.com/questions/561486/how-to-convert-an-integer-to-the-shortest-url-safe-string-in-python

# print(base64_bytes)


'''
number to based64Encoding
'''


# num = 1_000_000

# num_byte = bin(num)[2:]
# print(num_byte)


def make_encoder(baseString):
    size = len(baseString)
    d = dict((ch, i) for (i, ch) in enumerate(baseString))  # Map from char -> value
    if len(d) != size:
        raise Exception("Duplicate characters in encoding string")

    def encode(x):
        if x == 0:
            return baseString[0]  # Only needed if don't want '' for 0
        l = []
        while x > 0:
            l.append(baseString[x % size])
            x //= size
        return ''.join(l)

    def decode(s):
        return sum(d[ch] * size**i for (i, ch) in enumerate(s))

    return encode, decode


# Base 64 version:
encode, decode = make_encoder("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

assert decode(encode(435346456456)) == 435346456456


print(decode(encode(435346456456)))
