'''
61 · Search for a Range
462. Total Occurrence of Target
114 · First Position of Target

array = [5, 7, 7, 8, 8, 10]
target = 8

bisect_left
bisect_right

'''

from typing import (
    List,
)


class Solution:
    """
    @param a: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def search_range(self, a: List[int], target: int) -> List[int]:
        # write your code here
        start = self.bisect_left(a, target)
        end = self.bisect_right(a, target) - 1  # insertion point, could be out of bound

        if 0 <= start < len(a) and start <= end and a[start] == target:
            return [start, end]
        else:
            return [-1, -1]

    def bisect_left(self, a: List[int], target: int) -> int:
        lo, hi = 0, len(a)
        while lo < hi:
            mid = lo + (hi - lo) // 2

            if a[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

        # return bisect.bisect_left(a, target)

    def bisect_right(self, a: List[int], target: int) -> int:
        lo, hi = 0, len(a)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if a[mid] > target:
                hi = mid
            else:
                lo = mid + 1

        return lo


s = Solution()
#        0  1  2  3  4  5
array = [5, 7, 7, 8, 8, 10]
target = 8

res = s.search_range(array, target)
print(res)
