from typing import List


'''
Given an array of intervals intervals where intervals[i] = [start, end], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.



Solution 1: sort by starting time
Logic:

Attend the one with smaller start time first
(Greedy) Remove the one with bigger end time if overlapping occurs (because it will always incur more overlappings in the remaining array with asceding order of start time)
Example:

[[1,10], [2,3], [3,4], [5,6]]
First, we attend [1,10]
Next, [2,3] overlaps with [1,10] as 3 < 10. Here, we are going to remove [1,10] as it would definitely produce more overlappings as we continue the iteration.
Thirdly, attend [3,4]
Last, attend [5,6]


Time O(nlogn)

space O(1)

'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = float('-inf')
        res = 0

        for i in intervals:
            if i[0] >= prev:
                prev = i[1]
            else:
                ans += 1
                prev = min(prev, i[1])

        return res


so = Solution()

intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
res = so.eraseOverlapIntervals(intervals)


print(res)
