import collections
from typing import Deque, List
from collections import deque


# time O(mn)
# space O(mn)

ROOM = 2**31 - 1
GATE = 0
WALL = -1


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return

        m, n = len(rooms), len(rooms[0])
        queue = collections.deque([])

        # left right up down
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == GATE:
                    queue.append((i, j))

        dis = 0
        while queue:
            length = len(queue)
            dis += 1
            for i in range(length):
                curr = queue.popleft()
                for dir in dirs:
                    nextPos = (curr[0] + dir[0], curr[1] + dir[1])
                    if(nextPos[0] >= 0 and nextPos[0] < m and nextPos[1] >= 0 and nextPos[1] < n and rooms[nextPos[0]][nextPos[1]] == ROOM):
                        rooms[nextPos[0]][nextPos[1]] = dis
                        queue.append(nextPos)

        """
        Do not return anything, modify rooms in-place instead.
        """


solution = Solution()

rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]

solution.wallsAndGates(rooms)

print(rooms)
