
# We are working on a security system for a badged-access room in our company's building.

# We want to find employees who badged into our secured room unusually often. We have an unordered list of names and entry times over a single day. Access times are given as numbers up to four digits in length using 24-hour time, such as "800" or "2250".

# Write a function that finds anyone who badged into the room three or more times in a one-hour period. Your function should return each of the employees who fit that criteria, plus the times that they badged in during the one-hour period. If there are multiple one-hour periods where this was true for an employee, just return the earliest one for that employee.

# badge_times = [
#   ["Paul",      "1355"], ["Jennifer",  "1910"], ["Jose",    "835"],
#   ["Jose",       "830"], ["Paul",      "1315"], ["Chloe",     "0"],
#   ["Chloe",     "1910"], ["Jose",      "1615"], ["Jose",   "1640"],
#   ["Paul",      "1405"], ["Jose",       "855"], ["Jose",    "930"],
#   ["Jose",       "915"], ["Jose",       "730"], ["Jose",    "940"],
#   ["Jennifer",  "1335"], ["Jennifer",   "730"], ["Jose",   "1630"],
#   ["Jennifer",     "5"], ["Chloe",     "1909"], ["Zhang",     "1"],
#   ["Zhang",       "10"], ["Zhang",      "109"], ["Zhang",   "110"],
#   ["Amos",         "1"], ["Amos",         "2"], ["Amos",    "400"],
#   ["Amos",       "500"], ["Amos",       "503"], ["Amos",    "504"],
#   ["Amos",       "601"], ["Amos",       "602"], ["Paul",   "1416"],
# ];

# Expected output (in any order)
#    Paul: 1315 1355 1405
#    Jose: 830 835 855 915 930
#    Zhang: 10 109 110
#    Amos: 500 503 504

# n: length of the badge records array

from collections import defaultdict


def person(data):
    h_map = defaultdict(list)
    for name, time in data:
        h_map[name].append(int(time))

    res = []

    def getMinute(val: int):
        hour = val // 100
        minute = val - hour * 100

        total_minutes = hour * 60 + minute
        return total_minutes

    for k, v in h_map.items():
        v.sort()
        # print(v)
        n = len(v)

        for i in range(n-2):
            cur = v[i]
            third = v[i+2]

            if getMinute(third) - getMinute(cur) <= 60:
                time = [v[i], v[i+1], v[i+2]]

                j = i + 3
                while j < n:
                    if getMinute(v[j]) - getMinute(cur) <= 60:
                        time.append(v[j])
                    else:
                        break

                    j += 1

                res.append((k, time))
                break

    return res


badge_records = [
    ["Paul", "1355"],
    ["Jennifer", "1910"],
    ["Jose", "835"],
    ["Jose", "830"],
    ["Paul", "1315"],
    ["Chloe", "0"],
    ["Chloe", "1910"],
    ["Jose", "1615"],
    ["Jose", "1640"],
    ["Paul", "1405"],
    ["Jose", "855"],
    ["Jose", "930"],
    ["Jose", "915"],
    ["Jose", "730"],
    ["Jose", "940"],
    ["Jennifer", "1335"],
    ["Jennifer", "730"],
    ["Jose", "1630"],
    ["Jennifer", "5"],
    ["Chloe", "1909"],
    ["Zhang", "1"],
    ["Zhang", "10"],
    ["Zhang", "109"],
    ["Zhang", "110"],
    ["Amos", "1"],
    ["Amos", "2"],
    ["Amos", "400"],
    ["Amos", "500"],
    ["Amos", "503"],
    ["Amos", "504"],
    ["Amos", "601"],
    ["Amos", "602"],
    ["Paul", "1416"],
]

res = person(badge_records)

# print(res)

for item in res:
    print(item)
