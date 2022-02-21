from typing import List

'''
sort by meeting start time

check overlap


'''


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: [x[0], x[1]])

        for i in range(1, len(intervals)):
            pre_end = intervals[i-1][1]
            cur_start = intervals[i][0]
            if cur_start < pre_end:
                return False

        return True
