from typing import List


# brute force 3^n
#

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        memo = {}

        n = len(days)

        durations = [1, 7, 30]

        def dfs(i: int):
            if i == n:
                # if no days left 0 cost
                return 0

            if i in memo:
                return memo[i]

            memo[i] = float('inf')

            for d, c in zip(durations, costs):
                j = i

                # 1 7 or 30
                # binary search here
                #! ??
                while j < n and days[j] < days[i] + d:
                    j += 1
                memo[i] = min(memo[i], c + dfs(j))

            return memo[i]
        return dfs(0)


so = Solution()


days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]

res = so.mincostTickets(days, costs)

print(res)
