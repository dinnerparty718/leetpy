# find any peak

from typing import (
    List,
)


class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """

    def find_peak(self, a: List[int]) -> int:
        # write your code here
        l, r = 0, len(a)-1
        while l < r:
            mid = l + (r - l) // 2

            if a[mid] < a[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return l
