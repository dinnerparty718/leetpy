from typing import List
import heapq

# own


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heapq.heapify(intervals)

        meeting_room = []

        while len(intervals):
            meeting_start, meeting_end = heapq.heappop(intervals)
            # print(meeting_start, meeting_end)
            if not len(meeting_room) or meeting_start < meeting_room[0]:
                print(meeting_start)
                heapq.heappush(meeting_room, meeting_end)
            else:
                heapq.heappop(meeting_room)
                heapq.heappush(meeting_room, meeting_end)

        return len(meeting_room)

# sort interval directly


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0], reverse=True)

        meeting_room = []

        while len(intervals):
            meeting_start, meeting_end = intervals.pop()
            # print(meeting_start, meeting_end)
            if not len(meeting_room) or meeting_start < meeting_room[0]:
                #    print(meeting_start)
                heapq.heappush(meeting_room, meeting_end)
            else:
                heapq.heappop(meeting_room)
                heapq.heappush(meeting_room, meeting_end)

        return len(meeting_room)


intervals = [[0, 30], [5, 10], [15, 20]]
intervals = [[7, 10], [2, 4]]
so = Solution()


res = so.minMeetingRooms(intervals)
