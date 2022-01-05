from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pass


n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 1


so = Solution()

res = so.findCheapestPrice(n, flights, src, dst, k)


print(res)
