from typing import List


# Time O(n)
# space O(1)
# math formular
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        actual_sum = sum(nums)

        # formular

        #  1 + ...  n
        #  (n+1)n/2
        # expeted_sum = sum([i for i in range(1, n+1)])
        expeted_sum = (n+1) * n // 2

        return expeted_sum - actual_sum

# Time O(nlogn)
# space O(1) or O(n)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return len(nums)


so = Solution()

nums = [3, 0, 1]
res = so.missingNumber(nums)

print(res)
