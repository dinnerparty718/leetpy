from typing import List


# Time O(n)
# space O(1) using output array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = nums[:]

        num_of_zero = nums.count(0)

        if num_of_zero == len(nums):
            return [0] * n

        product = 1

        if num_of_zero == 0:
            for num in nums:
                product *= num

            for i in range(n):
                res[i] = int(product / res[i])
        elif num_of_zero == 1:
            for num in nums:
                if num != 0:
                    product *= num
            for i in range(n):
                if res[i] != 0:
                    res[i] = 0
                else:
                    res[i] = product
        else:
            return [0] * n

        return res


so = Solution()

nums = [-1, 1, 0, -3, 3]
res = so.productExceptSelf(nums)

print(res)
