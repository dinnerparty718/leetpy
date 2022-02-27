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

print(base64_bytes)
