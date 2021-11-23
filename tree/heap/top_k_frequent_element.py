from typing import List
from collections import Counter
import heapq


# own solution
# time
# build hashmap O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        print(m.keys())

        q = [(v, k) for k, v in m.items()]
        return [k[1] for k in heapq.nlargest(k, q)]


# leetcode
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)


so = Solution2()


nums = [3, 0, 1, 0]

k = 1


res = so.topKFrequent(nums, k)

print(res)
