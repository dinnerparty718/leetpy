from typing import List
import bisect


# own , kinda slow
# using bisect module log(n)
# Time O(nlogn)
# space O(n)


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        bisect.insort_left(intervals, newInterval)

        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            else:
                if res[-1][1] >= intervals[i][0]:
                    # merge
                    res[-1] = [min(res[-1][0], intervals[i][0]),
                               max(res[-1][1], intervals[i][1])]
                else:
                    res.append(intervals[i])

        return res


# one pass O(n)
# add orignal,
# once added, begin merging
# own good

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        i = 0

        # find insertion point

        while i < n and intervals[i][0] <= newInterval[0]:
            res.append(intervals[i])
            i += 1

        tmp = [newInterval] + intervals[i:]

        for i in range(len(tmp)):
            if not res or res[-1][1] < tmp[i][0]:
                res.append(tmp[i])
            else:
                res[-1] = [min(res[-1][0], tmp[i][0]),
                           max(res[-1][1], tmp[i][1])]

        return res


# leetcode
# O(n)
# similar to mine. avoid add interval and rest to form new array

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []

        # add all intervals starting before new Interval

        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1

        # add new inteval
        # if there is not interval
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], new_end)

        # add next intervals, merge with new Interval if nedded

        while idx < n:
            interval = intervals[idx]
            start, end = interval

            idx += 1

            # if there is no overlap , just add interval
            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], end)

        return output


so = Solution()

# intervals = [[1, 3], [6, 9]]
# newInterval = [2, 5]


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]


res = so.insert(intervals, newInterval)

print(res)
