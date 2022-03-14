from typing import List
from sortedcontainers import SortedList

'''
Brute Force
O(n^2)
for i in range(n):
    for j in range(j+1,n):

https://www.youtube.com/watch?v=wWrprKyQmE4

BIT

'''


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s = SortedList()
        output = []

        for n in nums[::-1]:
            ans = SortedList.bisect_left(s, n)
            output.append(ans)
            s.add(n)

        return output[::-1]


so = Solution()
nums = [5, 2, 6, 1]
# nums = [-1]
# nums = [-1, -1]
res = so.countSmaller(nums)

print(res)
