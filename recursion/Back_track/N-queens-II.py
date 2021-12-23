# https://leetcode.com/problems/n-queens-ii/solution/
# own solution
# remember current board state
class Solution:
    def totalNQueens(self, n: int) -> int:

        # 0 safe zone
        # -1 queen
        # 1 or more queen or under attack range
        board = [[0] * n for _i in range(n)]
        queen = set()

        def is_valid(i: int, j: int):
            return board[i][j] == 0

        def placeQueen(i: int, j: int):

            queen.add((i, j))
            # mark range
            board[i][j] = 9

            for col in range(n):
                if (i, col) not in queen:
                    board[i][col] += 1
            for row in range(n):
                if (row, j) not in queen:
                    board[row][j] += 1

            # dia \

            for row in range(n):
                for col in range(n):
                    if row - col == i - j and (row, col) not in queen:
                        board[row][col] += 1

            # dia /   j = (n-2-i)

            for row in range(n):
                for col in range(n):
                    if col + row == i+j and (row, col) not in queen:
                        board[row][col] += 1

        def removeQueen(i: int, j: int):

            # row
            for row in range(n):
                if (row, j) not in queen:
                    board[row][j] -= 1

            # col

            for col in range(n):
                if (i, col) not in queen:
                    board[i][col] -= 1

            # dia
            for row in range(n):
                for col in range(n):
                    if row - col == i - j and (row, col) not in queen:
                        board[row][col] -= 1

            for row in range(n):
                for col in range(n):
                    if col + row == i + j and (row, col) not in queen:
                        board[row][col] -= 1

            board[i][j] = 0
            queen.remove((i, j))

        def backtrack(row: int, count: int):
            for col in range(n):
                if is_valid(row, col):
                    placeQueen(row, col)

                    # base case each row has a queen
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack(row + 1, count)

                    removeQueen(row, col)

            return count

        res = backtrack(0, 0)

        return res


# Time complexity O(n!)
# space O(N)
# leetcode solution
# top down
# using single digit to represent col, diagonal, anti-diagonal
class Solution1:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int, diagonals: set, anti_diagonals: set, cols: set):
            if row == n:
                return 1

            solutions = 0

            for col in range(n):
                cur_diagonal = row - col
                cur_anti_diagonal = row + col

                if col in cols or cur_diagonal in diagonals or cur_anti_diagonal in anti_diagonals:
                    continue

                cols.add(col)
                diagonals.add(cur_diagonal)
                anti_diagonals.add(cur_anti_diagonal)
                solutions += backtrack(row+1, diagonals, anti_diagonals, cols)
                cols.remove(col)
                diagonals.remove(cur_diagonal)
                anti_diagonals.remove(cur_anti_diagonal)

            return solutions

        return backtrack(0, set(), set(), set())


so = Solution1()


n = 4

res = so.totalNQueens(n)
print(res)
