from typing import List
from collections import deque

# BFS or DFS


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q = deque([(sr, sc)])
        original_color = image[sr][sc]

        #! avoid infinit loop
        if original_color == newColor:
            return image

        image[sr][sc] = newColor

        m = len(image)
        n = len(image[0])

        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()

                for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                    if 0 <= I < m and 0 <= J < n and image[I][J] == original_color:
                        image[I][J] = newColor
                        q.append((I, J))

        return image


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        original_color = image[sr][sc]

        #! avoid infinit loop
        if original_color == newColor:
            return image

        image[sr][sc] = newColor

        m = len(image)
        n = len(image[0])

        def dfs(i: int, j: int):
            image[i][j] = newColor
            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < m and 0 <= J < n and image[I][J] == original_color:
                    dfs(I, J)

        dfs(sr, sc)

        return image


so = Solution()


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2


image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
newColor = 2


image = [[0, 0, 0], [0, 1, 1]]
sr = 1
sc = 1
newColor = 1

res = so.floodFill(image, sr, sc, newColor)

for row in res:
    print(row)
