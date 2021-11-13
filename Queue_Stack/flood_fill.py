from typing import List
from collections import deque

# https://leetcode.com/problems/flood-fill/discuss/626424/Python-sol-by-DFS-and-BFS-w-Comment

# own solution
# add visited set
# todo add dfs


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q = deque()
        original = image[sr][sc]

        if original == newColor:
            return image

        q.append((sr, sc))

        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                print(i, j)

                if 0 <= i < len(image) and 0 <= j < len(image[0]):
                    if image[i][j] != original:
                        continue
                    else:
                        image[i][j] = newColor
                        q.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])

        return image


# with visited set
class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q = deque()
        original = image[sr][sc]
        visited = set()
        q.append((sr, sc))

        while q:
            i, j = q.popleft()
            if 0 <= i < len(image) and 0 <= j < len(image[0]) and (i, j) not in visited:
                visited.add((i, j))
                if image[i][j] != original:
                    continue
                else:
                    image[i][j] = newColor
                    q.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])

        return image


so = Solution2()

image = [[0, 0, 0], [0, 1, 1]]
sr = 1
sc = 1
newColor = 1


res = so.floodFill(image, sr, sc, newColor)

print(res)
