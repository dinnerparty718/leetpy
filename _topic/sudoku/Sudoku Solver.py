'''

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.




'''


from typing import List
from collections import defaultdict


# much easy to understand
# standard dfs or backtrack. need to find the basecase
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board)

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        def box_index(i: int, j: int): return (i//3) * 3 + (j//3)

        #! fill up the sets first

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                val = int(board[i][j])

                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index(i, j)].add(val)

        def is_valid(i: int, j: int, val: int):
            box_idx = box_index(i, j)

            if val in rows[i] or val in cols[j] or val in boxes[box_idx]:
                return False
            return True

        def backtrack(i: int, j: int):
            # base case
            # left -> right, top -> bottom
            if i == n-1 and j == n:
                return True
            elif j == n:
                # move to the next row
                j = 0
                i += 1

            if board[i][j] != '.':
                return backtrack(i, j+1)

            for choice in range(1, n+1):
                if not is_valid(i, j, choice):
                    continue

                box_idx = box_index(i, j)

                # place
                board[i][j] = str(choice)
                rows[i].add(choice)
                cols[j].add(choice)
                boxes[box_idx].add(choice)

                if backtrack(i, j+1):
                    return True

                # remove
                board[i][j] = '.'
                rows[i].remove(choice)
                cols[j].remove(choice)
                boxes[box_idx].remove(choice)

            return False

        backtrack(0, 0)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


so = Solution()
res = so.solveSudoku(board)


for row in board:
    print(row)
