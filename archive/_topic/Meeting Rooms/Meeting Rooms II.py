import heapq
from typing import List
from sortedcontainers import SortedList

#  rooms = [] put end time the rooms Sorted List
#  use heap


# own


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        if len(intervals) <= 1:
            return len(intervals)

        rooms = [intervals[0][1]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # first item is the smallest
            if rooms[0] > start:
                heapq.heappush(rooms, end)
            else:
                heapq.heappop(rooms)
                heapq.heappush(rooms, end)

        return len(rooms)


class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms = []

        for start, end in intervals:
            if not rooms:
                rooms.append(end)
            else:
                # a roomt that < start

                if min(rooms) > start:
                    rooms.append(end)
                else:
                    # can be optizmied
                    for idx, room_end in enumerate(rooms):
                        if room_end <= start:
                            rooms[idx] = end
                            break

        return len(rooms)


so = Solution()


intervals = [[0, 30], [5, 10], [15, 20]]

intervals = [[7, 10], [2, 4]]

intervals = [[1293, 2986], [848, 3846], [4284, 5907],
             [4466, 4781], [518, 2918], [300, 5870]]
res = so.minMeetingRooms(intervals)
print(res)
