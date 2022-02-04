from typing import List


# must be O(n), can't use division

# own left -> right accumulative product
# right -> left accumulative product

# Time O(n)
# Space O(n) two intermediate array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_right = [1] * n
        right_left = [1] * n

        ans = [None] * n

        p = 1

        for idx, num in enumerate(nums):
            p *= num
            left_right[idx] = p

        p = 1

        for idx, num in enumerate(reversed(nums)):
            p *= num
            right_left[-idx - 1] = p

        for i in range(n):
            left = left_right[i-1] if i != 0 else 1
            right = right_left[i+1] if i != n-1 else 1

            ans[i] = left * right

        return ans


# Time O(n)
# Space O(1) without using extra space except output
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        # from left to right
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]

        p = 1

        for i in reversed(range(n)):
            ans[i] = ans[i] * p
            p *= nums[i]

        return ans


so = Solution()

#nums = [1, 2, 3, 4]

nums = [-1, 1, 0, -3, 3]

res = so.productExceptSelf(nums)


print(res)
