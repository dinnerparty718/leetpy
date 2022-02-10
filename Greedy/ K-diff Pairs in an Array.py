from collections import Counter
from typing import List
from unittest import result


# own slow hash
# use set to avoid duplicate
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        h_map = set()

        pair = set()

        for idx, num in enumerate(nums):
            complement_1 = k + num
            complement_2 = num - k

            if complement_1 in h_map:

                p = [complement_1, num]
                p.sort()
                pair.add(tuple(p))

            if complement_2 in h_map:
                p = [complement_2, num]
                p.sort()
                pair.add(tuple(p))

            h_map.add(num)

        return len(pair)


# brute force

# time O(n^2)

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        nums.sort()

        n = len(nums)
        res = 0

        for i in range(n):
            #! avoid duplicate
            if i == 0 or nums[i] != nums[i-1]:
                for j in range(i+1, n):
                    #! avoid duplicate
                    if j == i+1 or nums[j] != nums[j-1]:
                        if abs(nums[i] - nums[j]) == k:
                            res += 1

        return res

# modify two pointer approach
# left = 0, right = 1

# Time O(nlogn) from sort
# Space O(n) from sort


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, 1

        res = 0
        #! left could out of bound too
        while left < len(nums) and right < len(nums):
            if left == right or nums[right] - nums[left] < k:
                right += 1
            elif nums[right] - nums[left] > k:
                left += 1
            else:
                res += 1
                left += 1

                while left < len(nums) and nums[left] == nums[left - 1]:
                    left += 1

        return res


#! better hash

# Time O(n)
# Space O(n)

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0

        counter = Counter(nums)

        for x in counter:
            if k > 0 and x + k in counter:
                res += 1
            elif k == 0 and counter[x] > 1:
                res += 1
        return res


so = Solution()
nums = [3, 1, 4, 1, 5]
k = 2

res = so.findPairs(nums, k)


print(res)
