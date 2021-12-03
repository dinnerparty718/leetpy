# input '0000'
# output making one move. each position 2 value 2 * 4 = 8 combinations

from itertools import zip_longest
from typing import List


def neighbors(node: str) -> str:
    for i in range(4):
        x = int(node[i])
        for d in (-1, 1):
            y = (x + d) % 10
            yield node[:i] + str(y) + node[i+1:]


for i in neighbors('0000'):
    print(i)


def reverseStrnig(l: int, r: int, nums: List[int]):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1


str1 = '1234'
str2 = '234'


for d1, d2 in zip_longest(str1, str2, fillvalue='0'):
    print(d1, d2)
