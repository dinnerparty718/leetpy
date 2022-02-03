from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n < 3:
            return 0

        nums.sort()
        cnt = 0

        for i in range(n):
            lo = i + 1
            hi = n - 1

            while lo < hi:
                Sum = nums[i] + nums[lo] + nums[hi]

                if Sum < target:
                    cnt += hi - lo
                    lo += 1

                else:
                    hi -= 1

        return cnt


so = Solution()

nums = [-2, 0, 1, 3]
target = 2

# nums = [3, 1, 0, -2]
# target = 4


res = so.threeSumSmaller(nums, target)

print(res)
