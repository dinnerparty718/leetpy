from typing import List
from collections import deque

# room itself is a adjacent list


# own BFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        # entry point
        visited.add(0)

        q = deque(rooms[0])  # !important shouldput [0] instead of it's neibor

        while q:

            r = q.popleft()

            if r not in visited:
                visited.add(r)

            for room in rooms[r]:
                if room not in visited:
                    q.append(room)
                    visited.add(room)

        return len(visited) == len(rooms)

# BFS better


class Solution0:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)

        visited[0] = True

        q = deque([0])

        while q:
            cur = q.popleft()
            for nei in rooms[cur]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)

        return all(visited)

# DFS better


class Solution1:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)

        seen[0] = True
        stack = [0]

        while stack:
            node = stack.pop()

            for nei in rooms[node]:
                if not seen[nei]:
                    seen[nei] = True
                    stack.append(nei)

        return all(seen)


rooms = [[1, 3], [3, 0, 1], [2], [0]]
so = Solution0()

res = so.canVisitAllRooms(rooms)

print(res)
