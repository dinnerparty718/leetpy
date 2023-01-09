from typing import List

# todo DP
# https://leetcode.com/problems/split-array-largest-sum/

# binary search + greedy
# search space max(nums) + sum(nums)


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l = max(nums)
        r = sum(nums)

        def isValid(val: int):
            #! important
            cnt = 1
            cur_sum = 0

            for num in nums:
                if cur_sum + num > val:
                    cnt += 1
                    cur_sum = num
                else:
                    cur_sum += num

            return True if cnt <= m else False

        ans = r

        while l <= r:
            mid = l + (r-l) // 2

            if isValid(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1

        return ans


so = Solution()

nums = [7, 2, 5, 10, 8]
m = 2

# nums = [1, 4, 4]
# m = 3

res = so.splitArray(nums, m)
print(res)
