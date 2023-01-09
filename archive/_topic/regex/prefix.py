import re


file = '''
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

'''

#! ? optional 0 or one
pattern = re.compile(r'Mr\.?\s[A-Z]\w+')
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
#! group

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')


matches = pattern.finditer(file)

for match in matches:
    print(match)
