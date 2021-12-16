from typing import List

# own


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def keyFunction(item):
            return item[0]

        intervals = sorted(intervals, key=keyFunction)

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            prev = res[-1]
            # merge or append
            cur = intervals[i]

            if cur[1] >= prev[1] and cur[0] <= prev[1]:
                res[-1][1] = cur[1]
            elif cur[1] <= prev[1] and cur[0] <= prev[1]:
                continue
            else:
                res.append(cur)

        return res

# leet code


class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda n: n[0])

        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res


so = Solution()

intervals = [[1, 4], [3, 4]]
res = so.merge(intervals)


print(res)
