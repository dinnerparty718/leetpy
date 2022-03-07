from typing import List

'''
brute force (nm)^2
    for each cell, do dfs


better O(mn)
    dfs for all the nodes from both ocean


'''


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific, altantic = set(), set()

        def dfs(r: int, c: int, visited: set, prevHeight):
            if (r, c) in visited or (not (0 <= r < m and 0 <= c < n)) or heights[r][c] < prevHeight:
                return
            visited.add((r, c))

            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for col in range(n):
            dfs(0, col, pacific, heights[0][col])
            dfs(m-1, col, altantic, heights[m-1][col])

        for row in range(m):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, n-1, altantic, heights[row][n-1])

        return list(pacific.intersection(altantic))


so = Solution()


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]

res = so.pacificAtlantic(heights)

print(res)
