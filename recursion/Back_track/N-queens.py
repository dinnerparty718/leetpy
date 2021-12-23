from typing import List

# own solution
# Time complexity O(n!)
# Space O(n^2) for keeping track of the N * N board state


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        queens = []

        def backtrack(row: int, cols: set, dia: set, antidia: set, queenSet: set):
            if row == n:

                l = []

                for i in range(n):
                    cur_row = ''
                    for j in range(n):
                        if (i, j) in queenSet:
                            cur_row += 'Q'
                        else:
                            cur_row += '.'
                    l.append(cur_row)

                queens.append(l)
                return

            for col in range(n):
                if col in cols or row - col in dia or row + col in antidia:
                    continue

                cols.add(col)
                dia.add(row-col)
                antidia.add(row+col)
                queenSet.add((row, col))

                backtrack(row+1,  cols, dia, antidia, queenSet)

                cols.remove(col)
                dia.remove(row-col)
                antidia.remove(row + col)
                queenSet.remove((row, col))

        backtrack(0,  set(), set(), set(), set())

        return queens


class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def create_board(state):
            board = []
            for row in state:
                board.append(''.join(row))
            return board

        def backtrack(row: int, diagonals: set, anti_diagonals: set, cols: set, state: List[List[str]]):
            # base case
            if row == n:
                ans.append(create_board(state))
                return

            for col in range(n):
                cur_diagonal = row - col
                cur_anti_diagonal = row + col

                if col in cols or cur_diagonal in diagonals or cur_anti_diagonal in anti_diagonals:
                    continue

                cols.add(col)
                diagonals.add(cur_diagonal)
                anti_diagonals.add(cur_anti_diagonal)
                state[row][col] = 'Q'

                backtrack(row+1, diagonals, anti_diagonals, cols, state)

                cols.remove(col)
                diagonals.remove(cur_diagonal)
                anti_diagonals.remove(cur_anti_diagonal)
                state[row][col] = '.'

        empty_board = [['.'] * n for _ in range(n)]

        backtrack(0, set(), set(), set(), empty_board)
        return ans


so = Solution1()
n = 4
res = so.solveNQueens(n)


print(res)
