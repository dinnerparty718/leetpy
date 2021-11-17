# importing csv module
import csv

# csv file name
filename = "/Users/u1118608/leetpy/File/wip.csv"

# initializing the titles and rows list
fields = []
rows = []

d = {
    'BENEFITS_COVERAGE': [
        'SPECIALIST_CONSULTATION',
        'LAB_TEST',
        'DIAG_TEST',
        'HOME_VISIT',
        'PHYSIOTHERAPY',
        'DENTAL_TREATMENT',
        'DENTAL_SURGERY',
        'VACCINATION',
        'SPECIALIZED_OUTPATIENT',
        'OUTPATIENT_SURGERY',
        'INPATIENT',
        'CHILDBIRTH'
    ],
    'HEALTH_MANAGEMENT': [
        'CANCER_PREVENTION',
        'ROUTINE_TESTING',
        'HEALTHY_EATING',
        'OBESITY_DIABETES_PREVENTION',
        'PHYSICAL_ACTIVITY',
        'STRESS_MANAGEMENT',
        'SMOKING_CESSATION',
        'BACK_PAIN_PREVENTION',
        'OTHER_HEALTH_MGMT'
    ],
    'OTHER_FEATURES': [
        'OCCUPATIONAL_MEDICINE',
        'SSC_OPTIMIZATION',
        'COST_REIMBURSEMENT',
        'SENIOR_PACKAGE',
        'EMPLOYER_CONTRIBUTION',
        'FAMILY_PACKAGE'
    ],
    'RATE_INFORMATION': [
        'PREMIUM_EMPLOYEE',
        'SURCHARGE_EMPLOYEE',
        'PREMIUM_PARTNER',
        'SURCHARGE_PARTNER',
        'PREMIUM_FAMILY',
        'SURCHARGE_FAMILY'
    ]
}

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# 12 + 9 + 6 + 6


res = []
new_fields = fields[:6]
new_fields[0] = 'CARRIER'
new_fields.append('CATEGORY')
new_fields.append('SUB_CATEGORY')
new_fields.append('VALUE')

print(new_fields)

for record in rows:
    # tmp = []
    for key, values in d.items():
        for sub in values:
            common = record[:6]
            common.append(key)
            common.append(sub)

            idx = fields.index(sub)
            common.append(record[idx])
            res.append(common)
        # tmp.append(common)

    # print(tmp)

    # res.extend(tmp)

# with open('./File/output.csv', 'w') as f:
#     write = csv.writer(f)
#     write.writerow(new_fields)
#     write.writerows(res)


print(len(res))
