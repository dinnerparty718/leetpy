from typing import List


# Stack
# scan num2 once and put result in hahs
# time O(n) n is the length of nums2 (nums1 is a subset)

# space O(n)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_map = {}

        stack = []

        result = [-1] * len(nums1)

        for i, num in enumerate(nums2):
            while stack and nums2[stack[-1]] < num:
                idx = stack.pop()
                next_map[nums2[idx]] = num

            stack.append(i)

        # stack could have value left
        print(stack)

        for idx, n in enumerate(nums1):
            if n in next_map:
                result[idx] = next_map[n]

        return result


so = Solution()


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]

res = so.nextGreaterElement(nums1, nums2)


print(res)
