# https://leetcode.com/problems/number-of-islands/discuss/345981/Python3Number-of-Islands-BFS-%2B-DFS
from typing import List
from collections import deque


# modified the input
# time O(M×N)
# space O(min(M,N)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,NM,N).
# Maximum siblings in queue will be min(M, N) https://imgur.com/gallery/M58OKvB


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        queue = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append((i, j))
                    self.helper(grid, queue)
                    count += 1

        return count

    def helper(self, grid, queue):
        while queue:
            I, J = queue.popleft()
            for i, j in [I + 1, J], [I - 1, J], [I, J + 1], [I, J - 1]:
                if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append((i, j))


solution = Solution()


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]


]

res = solution.numIslands(grid)


print(res)
