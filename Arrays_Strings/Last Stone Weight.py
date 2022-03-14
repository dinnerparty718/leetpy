from typing import List

import heapq


'''
O(nlogn)

'''


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)

            first = -first
            second = - second

            if second != first:
                heapq.heappush(stones, -(first - second))

        stones.append(0)

        return abs(stones[0])


stones = [2, 7, 4, 1, 8, 1]

so = Solution()

res = so.lastStoneWeight(stones)

print(res)
