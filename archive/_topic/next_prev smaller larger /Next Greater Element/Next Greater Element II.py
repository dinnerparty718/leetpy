

from typing import List

# circular style, is not found -1
# yass!
# stack
# Time O(n)
# Space O(n)


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [-1] * n
        stack = []

        for i in range(2*n):
            idx = i % n

            while stack and nums[stack[-1]] < nums[idx]:
                next_idx = stack.pop()

                # if output[next_idx] == None:
                output[next_idx] = nums[idx]

            stack.append(idx)

        return output


so = Solution()

nums = [1, 2, 1]
#nums = [1, 2, 3, 4, 3]
res = so.nextGreaterElements(nums)

print(res)
