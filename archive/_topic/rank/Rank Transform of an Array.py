from typing import List


'''
sort


Time O(NlogN)
Space O(N)


'''


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # avoid duplicate
        rank = {}
        for a in sorted(arr):
            rank.setdefault(a, len(rank) + 1)

        return [rank[num] for num in arr]


arr = [40, 10, 20, 30]
arr = [100, 100, 100]


so = Solution()

res = so.arrayRankTransform(arr)

print(res)
