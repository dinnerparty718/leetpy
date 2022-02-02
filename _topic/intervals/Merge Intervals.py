from typing import List


# assuming not sorting?

# Time O(nlogn)
# space O(n)


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        output = []

        for i in range(len(intervals)):

            start, end = intervals[i]

            if not output or start > output[-1][1]:
                output.append(intervals[i])
            else:
                output[-1][1] = max(output[-1][1], end)

        return output


intervals = [[1, 4], [4, 5]]


so = Solution()

res = so.merge(intervals)


print(res)
