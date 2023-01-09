import re


file = '''
Dave Martin
615-555-7164
173 Main St. Springfield RI 55924
davemartin@bogusmeail.com


Dave Bob
123-345-7888
173 Main St. Springfield RI 55924
davemartin@fakemeail.com



Dave Bob
808.333.7338
173 Main St. Springfield RI 55924
davemartin2@fakemeail.com


Dave Bob
808*333*7338
173 Main St. Springfield RI 55924
davemartin2@fakemeail.com


800-333-7338
900-333-7338


'''

pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')
pattern = re.compile(r'[89]\d\d[-.]\d\d\d[-.]\d\d\d\d')
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

matches = pattern.finditer(file)

for match in matches:
    print(match)
