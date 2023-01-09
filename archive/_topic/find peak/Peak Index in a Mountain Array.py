

from typing import List


# binary search
# O(logn)

'''
binary search

l < r

if mid < mid+1:
    l = mid + 1
else:
    r = mid
return r

'''


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1

        while l < r:
            mid = l + (r-l) // 2

            #! safty can +1 since arr[mid] is not answer for sure
            if arr[mid] < arr[mid+1]:
                l = mid+1
            else:
                r = mid

        return r

        # one pass method
        # o(n)


so = Solution()

arr = [0, 1, 0]
# arr = [0, 2, 1, 0]
# arr = [0, 10, 5, 2]
res = so.peakIndexInMountainArray(arr)

print(res)
