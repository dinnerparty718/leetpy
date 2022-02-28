from utils.number_conver import numStr


# a = 400_200_000
# print(numStr(a))

# number
one_tri = 1_000_000_000_000
one_b = 1_000_000_000
one_m = 1_000_000


# time
sec_in_a_day = 86_400


# storage
def byte_to_large(b: int, deno: str):
    conversion = {
        'GB': 1073741824,
        'TB': 1099511627776,
        'PB': 1125899906842624
    }

    if deno not in conversion:
        print('wrong input')
        return

    val = b / conversion[deno]
    valStr = numStr(val) + f' {deno}'
    print(f'{val:.2f}', '\t', valStr)


byte_to_large(one_tri, 'GB')


# bandwidth Mbps - megabits per second


byte_to_large(15*one_b * 8, 'GB')
