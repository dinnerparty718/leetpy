from typing import List


# two pointer
# o(n) single pass

'''
l, r = 0, len(height) -1

global res = 0


while l < r:
    area = (r-l) * min (left height, right height)
    update global
    
    if left < right:
        l+=1
    elf:
        r -=1
    
return global res




'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = 0
        l, r = 0, len(height)-1

        max_val = 0

        while l < r:
            area = (r-l) * min(height[l], height[r])
            max_val = max(max_val, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_val


# brute force
# time O(n^2)
# space 0(1)


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = 0

        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = (j - i) * min(height[i], height[j])

                max_val = max(area, max_val)

        return max_val


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [1, 2, 4, 3]
height = [1, 1]

so = Solution()

res = so.maxArea(height)

print(res)
