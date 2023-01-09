import re


'''

.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitesapce (space, tab, newline)



 -----

\b      - Word Boundary
\B      - Not a Word boundary
^       - Begining of a String
$       - End of a String


[]      - Matches Characters in brackets
[^ ]    - Macches Characters Not in brakets
|       - Either Or
()      - Group


Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (min,max)






'''

group = ['apple apple', 'apple anything orange']
shoppingCart = ['apple', 'apple']


# raw string

# print(r'\tTab')


text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha Haha

MegaCharacters (Need to be escaped):

. ^ $ * + ? { } [ ] | | ( )

corems.com


321-555-4321
123.555.1234
123*555*1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
,


cat
mat
pat
bat

'''


pattern = re.compile(r'abc')

#! MegaCharacters
#! ',' comma does not need to match

pattern = re.compile(r',')


#! pattern.findall()
maches = pattern.finditer(text_to_search)


for match in maches:
    # <re.Match object; span=(1, 4), match='abc'>
    print(match.start())

# \BHa
pattern = re.compile(r'\bHa')


maches = pattern.finditer(text_to_search)

# for match in maches:
#     print(match)


# sentence = 'Start a sentence and then brign it to an end'
# pattern = re.compile(r'end$')

# maches = pattern.finditer(sentence)


# for match in maches:
#     print(match)


#! - between something

pattern = re.compile(r'[1-5]')
pattern = re.compile(r'[a-zA-Z]')


#! carat in character set means NOT
pattern = re.compile(r'[^a-zA-Z]')


# not b
pattern = re.compile(r'[^b]at')


maches = pattern.finditer(text_to_search)

# for match in maches:
#     print(match)


# match in the begining
# pattern.match()


sentence = 'Start a sentence and then brign it and to an end'

pattern = re.compile(r'and')


# start from index
matches = pattern.search(sentence, 30)

print(matches.start())
print(matches.end())


#! flag -ignore cases


pattern = re.compile(r'start', re.IGNORECASE)
pattern = re.compile(r'start', re.I)


matches = pattern.search(sentence)

print(matches.group())
