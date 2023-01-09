from typing import List

import heapq

# todo quick select algo


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not k or not points:
            return []

        dist = []
        res = []
        for idx, p in enumerate(points):
            x, y = p

            distance = (abs(x)**2 + abs(y)**2) ** 0.5
            dist.append((distance, idx))

        heapq.heapify(dist)

        while k > 0:
            dis, idx = heapq.heappop(dist)
            res.append(points[idx])
            k -= 1

        return res


points = [[3, 3], [5, -1], [-2, 4]]
k = 2


so = Solution()

res = so.kClosest(points, k)

print(res)
