from tkinter.tix import Tree
from typing import List

'''
equivilant
longest susbtring with at most 2 char
'''


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        end = 0
        max_len = 0
        d = {}  # store type: index

        while end < len(fruits):
            d[fruits[end]] = end
            if len(d) >= 3:
                min_val = min(d.values())
                del d[fruits[min_val]]
                start = min_val+1

            max_len = max(max_len, end - start + 1)
            end += 1

        return max_len
