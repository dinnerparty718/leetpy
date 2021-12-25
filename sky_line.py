from typing import List

# https://leetcode.com/problems/the-skyline-problem/discuss/61261/10-line-Python-solution-104-ms

import heapq

from sortedcontainers import SortedList


# class maxpq:
#     def __init__(self) -> None:
#         self.container = []

#     def front(self):
#         return 0 if not self.container else -self.container[0]

#     def push(self, h):
#         heapq.heappush(self.container, -h)

#     # linear time
#     def remove(self, h):
#         print(self.container, -h)
#         self.container.remove(-h)
#         heapq.heapify(self.container)


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []  # (x, height, isEntryEvent)
        for l, r, h in buildings:
            events.append((l, h, -1))
            events.append((r, h, 1))

        # sort by x,  then by type (start < end ), then by height * type
        events.sort(key=lambda x: [x[0], x[2], x[2] * x[1]])

        print(events)

        skyline = []
        # pq = maxpq()

        sortedList = SortedList([0])

        for x, h, type in events:
            if type == -1:  # entry
                # if h > pq.front():
                #     skyline.append([x, h])
                # pq.push(h)

                if h > sortedList[-1]:
                    skyline.append([x, h])
                sortedList.add(h)
            else:
                # pq.remove(h)
                # skyligh drop
                # if h > pq.front():
                #     skyline.append([x, pq.front()])

                sortedList.discard(h)
                if h > sortedList[-1]:
                    skyline.append([x, sortedList[-1]])

        return skyline


so = Solution()

buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
res = so.getSkyline(buildings)


print(res)


# # test sorting and special cases

# buildings_side_by_side = [[2, 4, 8], [4, 6, 10]]

# # sort by height descending use -1 as trick Tall -> short
# buildings_with_same_entry = [[2, 4, 10], [2, 6, 12], [2, 8, 14]]

# # sort by height descending  Short -> Tall
# buildings_with_same_exit = [[2, 8, 14], [4, 8, 12], [6, 8, 10]]

# e = []

# for l, r, h in buildings_with_same_exit:
#     e.append((l, h, -1))
#     e.append((r, h, 1))


# e.sort(key=lambda x: [x[0], x[2], x[2] * x[1]])


# for i in e:
#     print(i)
