
# 2147483647
MAX = 2 ** 31 - 1

# -2147483648
MIN = - 2 ** 31


str = '214748364'
str = '214748364'


# [ -2 ** 31 , 2 **31 - 1 ]
# if out of bound , return MIN or MAX
def str_to_number(num: str, sign: str):

    i = 0
    res = 0
    while i < len(num):
        val = int(num[i])

        if sign == '+':
            if res > MAX // 10 or (res == MAX // 10 and val > 7):
                return MAX

        else:
            if res > MAX // 10 or (res == MAX // 10 and val > 8):
                return MIN

        res = res * 10 + val
        i += 1

    return res if sign == '+' else -res


val = str_to_number(str, '-')

print(val)
