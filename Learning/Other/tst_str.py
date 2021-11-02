# string
# single or double quote
# long str

'hi hello'

"hi hello"


print(type("ehy"))


long_string = '''
hello!!

WHO

'''

first_name = 'yy'
last_name = 'chen'

# join    order is reverse
# ' '.join(list)


print(', '.join((first_name, last_name)))

# concatenation only works with strinig
# print('hello' + 5) error

print('hello' + str(5)) # type conversion

# escape sequence

weather = 'it\'s sunny'
weather = "it's sunny"
weather = 'it\'s \"kind of\" sunny'

print(weather)

print('\\')
print('\tabc') # \t adding a tab
print('\n')
print('hope you have a good day')


# string formatting

name = 'Johnny'
age = 45

print('hi '+ name+ '. you are at '+ str(age)+ ' years old')


#prefer way similary to `` in javascript
print(f'hi {name} is at {age} years old')




# string index
# string is iterator

# for i in 'me meme':
#     print(i)


selfish = '01234567'

# string slicing
# [start:stop:stepover] stepover default to 1

print(selfish[0:11])
print(selfish[1:])
print(selfish[:3])
print(selfish[:])

print(selfish[-1]) # last item

print(selfish[::-1]) # reverse a string


# len

print(len(selfish))


# built-in function  print() len() str()
# build-in method, owned something  start with .


quote = 'to be or not bo be'

print(quote.count('t'))
print(quote.upper()) # lower
print(quote.capitalize()) # capitalize the begining of the sentense
print(quote.find('to')) # if == 0 start of the string


print(quote.replace('be','me'))

print(quote) # immutable


words = quote.split(' ')
print(words)

#  The str.split() method without an argument splits on whitespace:

words = "many   fancy word \nhello    \thi".split()
print(words)