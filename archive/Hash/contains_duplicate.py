from typing import List

# using set 1


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

so = Solution2()

print(so.containsDuplicate(nums))
