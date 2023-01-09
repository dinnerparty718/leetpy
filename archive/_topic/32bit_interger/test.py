
# 2147483647
MAX = 2 ** 31 - 1

# -2147483648
MIN = - 2 ** 31


# [ -2 ** 31 , 2 **31 - 1 ]
# if out of bound , return MIN or MAX


def to_number(num_str: str):

    if not num_str:
        return 0

    INT_MAX = pow(2, 31) - 1
    INT_MIN = - pow(2, 31)

    sign = 1
    res = 0

    i = 0

    if i < len(num_str) and num_str[i] == '-':
        i += 1
        sign = -1
    if i < len(num_str) and num_str[i] == '+':
        i += 1
        sign = 1

    while i < len(num_str) and num_str[i].isdigit():

        digit = int(num_str[i])

        if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > MAX % 10):
            return INT_MAX if sign == 1 else INT_MIN

        res = res * 10 + digit
        i += 1

    return res * sign


str = '214748364'
str = '-2147483649'


val = to_number(str)

print(val)
