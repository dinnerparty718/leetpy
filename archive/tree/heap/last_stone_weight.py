from typing import List
import heapq


# own simimar with best python solution
# time heapify O(n)
# time pop and add O(logn)
# total time O(Nlogn)
# space python heapify O(1)
# space java O(n)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # max heap
        maxHeap = [stone * -1 for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            l, s = abs(heapq.heappop(maxHeap)), abs(heapq.heappop(maxHeap))
            if l != s:
                heapq.heappush(maxHeap, s - l)

        return abs(maxHeap[0]) if len(maxHeap) else 0


so = Solution()


stones = [2, 7, 4, 1, 8, 1]


res = so.lastStoneWeight(stones)

print(res)
