from typing import List
from functools import lru_cache


'''

Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.




DP
dp = [[0] * (m+1) for _ in range(m+1)]


#! basecase
    0000
    0000
    0000
    
#! recurrence
    from right -> left bottom up  
    
    only visit half of dp
    
    for i in range(m-1,-1, -1)
        for j in range(i ,-1 ,-1)    j  is left index -> right index k = n - 1 - (i - j)
    
    [14, 0, 0, 0]
    [5,  8, 0, 0]
    [1,  2, 3, 0]
    [0,  0, 0, 0]
    
    multi = multipliers[i]
    k =  n - 1 - (i - j)

    dp[i][j] = max(multi* nums[j] + dp[i+1][j+1], multi*nums[i] + dp[i+1][j]  )
        
#! return dp[0][0]

'''

#! i + right-left + 1 = n
#! right = n - 1 + left - i
#! right = n - 1 - (i - left)


# bottom up
# start from base case i == m

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                # use left                             or   use right
                dp[i][left] = max(mult * nums[left] + dp[i+1][left+1],    dp[i+1][left] + mult * nums[right])

        # for row in dp:
        #     print(row)

        return dp[0][0]


# top down
# time limit or memery limit

#! exceed limit


class Solution1:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        n = len(nums)
        m = len(multipliers)

        # state i, left, right

        # dp return max score after i interation
        # dp(0,0)

        @lru_cache(2000)
        def dfs(i: int, left: int) -> int:
            if i == m:
                return 0
            mult = multipliers[i]
            right = n - 1 - (i - left)
            return max(dfs(i+1, left+1) + mult * nums[left], dfs(i+1, left) + mult * nums[right])

        res = dfs(0, 0)

        #! clear the cache before returning
        dfs.cache_clear()
        return res


so = Solution()


nums = [1, 2, 3]
multipliers = [3, 2, 1]

# nums = [-5, -3, -3, -2, 7, 1]
# multipliers = [-10, -5, 3, 4, 6]

res = so.maximumScore(nums, multipliers)

print(res)


#! range(start, stop, step)

# l = ['a', 'b', 'c', 'd', 'e']

# for i in range(len(l)-1, -1, -1):
#     print(l[i])
