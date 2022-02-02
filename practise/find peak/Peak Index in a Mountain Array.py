

from typing import List


# binary search
# O(logn)

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1

        while l < r:
            mid = l + (r-l) // 2

            if arr[mid] < arr[mid+1]:
                l = mid+1
            else:
                r = mid

        return r

        # one pass method
        # o(n)


class Solution1:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak_idx = 0

        if len(arr) == 1:
            return 0

        for i in range(len(arr)):
            if arr[i] > arr[peak_idx]:
                peak_idx = i

        return peak_idx


so = Solution()

arr = [0, 1, 0]
# arr = [0, 2, 1, 0]
# arr = [0, 10, 5, 2]
res = so.peakIndexInMountainArray(arr)

print(res)
