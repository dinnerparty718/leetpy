import sys


# ['/Users/u1118608/leetpy/test_sys.py']
print(sys.argv)
# first index is the file name

first = sys.argv[1]
last = sys.argv[2]

print((' ').join([first, last]))
