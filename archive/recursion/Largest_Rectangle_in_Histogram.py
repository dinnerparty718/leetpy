from typing import List
# Time O(n^2)
# O(1)
# more of a stack problem
# https://leetcode.com/problems/largest-rectangle-in-histogram/solution/


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)

        res = 0

        for i in range(n):

            min_height = float('inf')
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                res = max(res, (j-i+1) * min_height)

        return res

# stack, check temperature s
# O(n)
# O(n)


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maxArea = float('-inf')

        for i in range(len(heights)):
            while(stack[-1] != -1 and heights[stack[-1]] >= heights[i]):
                cur_heigth = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                maxArea = max(maxArea, cur_heigth * cur_width)
            stack.append(i)

        while stack[-1] != -1:
            cur_heigth = heights[stack.pop()]
            cur_width = len(heights) - stack[-1] - 1
            maxArea = max(maxArea, cur_heigth * cur_width)

        return maxArea

# divide and conqure


class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def calculateArea(start: int, end: int):
            if start > end:
                return 0

            min_index = start
            for i in range(start, end+1):
                if heights[i] < heights[min_index]:
                    min_index = i

            #
            cur = heights[min_index] * (end-start + 1)

            left = calculateArea(start, min_index-1)
            right = calculateArea(min_index+1, end)

            return max(cur, left, right)

        return calculateArea(0, len(heights)-1)


so = Solution1()

heights = [2, 4]
res = so.largestRectangleArea(heights)


print(res)
