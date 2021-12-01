import json
import csv


# Opening JSON file
f = open('plan_design.json')

# returns JSON object as
# a dictionary
data = json.load(f)


# Closing file
f.close()


f2 = open('plan_detail.json')

# returns JSON object as
# a dictionary
data2 = json.load(f2)


# Closing file
f2.close()

# for k, v in data.items():
#     print(k, v)

# with open('./File/output.csv', 'w') as f:
#     write = csv.writer(f)
#     write.writerow(new_fields)
#     write.writerows(res)

res = []

design = 'DESIGN'
detail = 'DETAIL'

for k, v in data.items():
    for item in v:
        res.append([k, design, item])


for k, v in data2.items():
    for item in v:
        res.append([k, detail, item])


with open('plan_design_detail.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(['COUNTRY_CODE', 'TYPE', 'ATTRIBUTE'])
    write.writerows(res)
