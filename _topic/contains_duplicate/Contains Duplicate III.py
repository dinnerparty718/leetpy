import sortedcontainers
from typing import List
from sortedcontainers import SortedList


# BST TreeMap in java
# sorted dict in python

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        def lowerBound(num: int, bst: SortedList):
            idx = bst.bisect_right(num) - 1
            return bst[idx] if idx >= 0 else None

        def upperBound(num: int, bst: SortedList):
            idx = bst.bisect_right(num)
            return bst[idx] if idx < len(bst) else None

        seen = SortedList()

        for i, num in enumerate(nums):
            left = lowerBound(num, seen)

            #! is not None  VS if not left  are not the same
            if left is not None and num - left <= t:
                return True

            right = upperBound(num, seen)
            if right is not None and right - num <= t:
                return True

            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i-k])

        return False


# leetcode
# much better logic
class Solution1:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        # lower bound, if there a duplicate
        def floor(n, bst):
            le = bst.bisect_right(n) - 1
            return bst[le] if le >= 0 else None

        def ceiling(n, bst):
            ge = bst.bisect_right(n)
            return bst[ge] if ge < len(bst) else None

        bst = sortedcontainers.SortedList()
        for i, n in enumerate(nums):
            le = floor(n, bst)
            # check left first,
            if le is not None and n <= le + t:
                return True
            ge = ceiling(n, bst)
            # then check right
            if ge is not None and ge <= n + t:
                return True
            bst.add(n)
            if len(bst) > k:
                bst.remove(nums[i-k])
        return False
    # time:  O(nlogk)
    # space: O(k)


so = Solution()

# nums = [1, 2, 3, 1]
# k = 3
# t = 0

# nums = [1, 0, 1, 1]
# k = 1
# t = 2

# nums = [1, 5, 9, 1, 5, 9]
# k = 2
# t = 3

nums = [-3, 3, -6]
k = 2
t = 3

res = so.containsNearbyAlmostDuplicate(nums, k, t)

print(res)


# remove 1

# a = SortedList([1, 5, 9])


# a.remove(1)

# print(a)
