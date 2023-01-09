from typing import List
from sortedcontainers import SortedList


# syntax can to optimized
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}

        for idx, n in enumerate(nums):
            if n not in m:
                m[n] = idx
            else:
                # find duplicate
                if abs(idx - m[n]) <= k:
                    return True
                else:
                    m[n] = idx

        return False


class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}

        for idx, n in enumerate(nums):
            if n in m and idx - m[n] <= k:
                return True
            m[n] = idx

        return False


so = Solution()

nums = [1, 0, 1, 1]
k = 1


res = so.containsNearbyDuplicate(nums, k)

print(res)
