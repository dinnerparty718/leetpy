from typing import List

# dfs or backtrack

# time O(N * 3^L) N is number of cell, 4 -1  direction
# 3-ary tree
# space O(L) for call back


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i: int, j: int, suffix: str):

            if len(suffix) == 0:
                return True

            # check boundaries

            #! This is an important choice though. Doing the boundary check within the function would allow us to reach the bottom case, for the test case where the board contains only a single cell, since either of neighbor indices would not be valid.

            if i < 0 or i == m or j < 0 or j == n or board[i][j] != suffix[0]:
                return False

            board[i][j] = '#'

            # to be able to reach the base case

            for i_offset, j_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if dfs(i + i_offset, j + j_offset, suffix[1:]):
                    return True

            board[i][j] = suffix[0]

            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, word):
                    return True

        return False


so = Solution()

# board = [
#     ["A", "B", "C", "E"],
#     ["S", "F", "C", "S"],
#     ["A", "D", "E", "E"]
# ]
# word = "ABCCED"

# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "SEE"

# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCB"


# board = [["a", "a"]]
# word = "aaa"

# ! edge case
board = [["a"]]
word = "a"

res = so.exist(board, word)

print(res)
