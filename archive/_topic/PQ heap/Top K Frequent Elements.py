import heapq
from typing import List
from collections import defaultdict

# count , heapify
# max heap
# Time O(nlogk)
# space O(n)

# todo quick select

# https://leetcode.com/problems/top-k-frequent-elements/solution/


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)

        for num in nums:
            cnt[num] += 1

        max_heap = [(-cnt, num) for num, cnt in cnt.items()]

        heapq.heapify(max_heap)

        res = []

        while k > 0:
            cnt, num = heapq.heappop(max_heap)
            res.append(num)
            k -= 1

        return res


so = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2

nums = [1]
k = 1

res = so.topKFrequent(nums, k)

print(res)
