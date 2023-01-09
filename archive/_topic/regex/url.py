import re


file = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

'''

#! grab to sub string, using group
#! group 0 is the entire ting

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = pattern.finditer(file)

for match in matches:
    # print(match.group())
    print(match.group(2), match.group(3))


# subbed_urls = pattern.sub(r'\2\3', file)

# print(subbed_urls)


matches = pattern.findall(file)

'''
('www.', 'google', '.com')
('', 'coreyms', '.com')
('', 'youtube', '.com')
('www.', 'nasa', '.gov')

'''

for match in matches:
    print(match)  # only print groups
