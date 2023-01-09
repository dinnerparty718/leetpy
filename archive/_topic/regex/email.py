import re


file = '''
CoreyMSchfer@gamil.com
corey.schafer@uniersity.edu
corey-321-schafer@my-work.net

'''

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')


pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+')

matches = pattern.finditer(file)

for match in matches:
    print(match)
