'''
Faster then list
Represent a queue

use deque for both stack and queue

deque('hello',maxlen=5)

append()
appendleft()
pop()
popleft()

extend() add iterables to exisiting deque
clear()
rotate(n)



'''

from collections import deque


d = deque()

d.append(4)
d.append(5)

print(d)


d.appendleft(1)
d.appendleft(1)



c = d.popleft()

print(c)


c = deque('hello')
print(c)

c.clear()

print(c)

c = deque('hi')


c.extend('YY')

# adding to the left one by one
c.extendleft('be')

print(c)


d = deque('hello', maxlen=5)

print(d.maxlen)
# cant change maxlen after creating deque

print(d)

d.extend('word')

print(d)
