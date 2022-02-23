
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

    res2 = []

    for k, v in h_map.items():
        v.sort()
        # print(v)
        n = len(v)

        # for i in range(n-2):
        #   cur = v[i]
        #   third = v[i+2]
        #   # 1350 1355
        #   h_cur =  cur // 100  #13
        #   min_cur = cur - h_cur * 100

        #   h_third = third // 100
        #   min_third = third - h_third * 100

        #   cur_minute = h_cur * 60 + min_cur
        #   third_minute = h_third * 60 + min_third

        #   if third_minute - cur_minute <= 60:
        #     # print(i,

        #     # if k == 'Jennifer':
        #     #   print('DEBGU',cur_minute,third_minute )
        #     res.append((k,v[i],v[i+1], v[i+2] ))
        #     break

        r = 0
        start_min = None
        local_res = []

        while r < n:
            cur_min = (v[r] // 100) * 60 + (v[r] - (v[r] // 100) * 100)

            if start_min is None:
                start_min = cur_min
                local_res.append(start_min)
            else:
                if cur_min - start_min <= 60:
                    r += 1
                    local_res.append(cur_min)
                else:
                    start_min = None
                    local_res = []

        if len(local_res) >= 3:
            res2.append((k, local_res))

    return res2


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

print(res)
