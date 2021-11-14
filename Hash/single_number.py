from collections import Counter
from typing import List

# own
# time O(n)
# space O(n)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()

        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return s.pop()

# own
# time O(n)
# space O(n)


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        d = Counter(nums)
        for k, v in d.items():
            if v < 2:
                return k

# XOR
# x ^ x = 0
# y ^ y = 0
# time O(n)
# space O(1)


class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result


so = Solution3()

nums = [4, 1, 2, 1, 2]


print(so.singleNumber(nums))
