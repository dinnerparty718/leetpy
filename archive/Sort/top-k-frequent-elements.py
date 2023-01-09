from typing import List
from collections import Counter


# own
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        cnt = Counter(nums)

        buckets = [None] * (n+1)

        for key, count in cnt.items():
            if buckets[count] == None:
                buckets[count] = [key]
            else:
                buckets[count].append(key)

        # print(buckets)

        res = []

        for i in reversed(range(1, n+1)):
            if buckets[i] != None:
                while buckets[i]:
                    res.append(buckets[i].pop())
                    k -= 1

                    if k == 0:
                        return res


# better coding style

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        res = []

        # descending order
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


so = Solution()


# nums = [1, 1, 1, 2, 2, 3]
# k = 2

nums = [1]
k = 1

res = so.topKFrequent(nums, k)

print(res)
