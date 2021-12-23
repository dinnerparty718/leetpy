from typing import List


# 3 * 3
# own
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = 9

        nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        def moveToNext(i: int, j: int):
            if j == 8:
                return (i+1, 0)
            else:
                return (i, j+1)
            # return

        def getSubGroupRange(idx: int):
            if idx >= 6:
                return [6, 7, 8]
            elif idx >= 3:
                return [3, 4, 5]
            else:
                return [0, 1, 2]

        def backtrack(row: int, col: int):
            nonlocal res
            if row == n:
                res = [row[:] for row in board]

                return

            # print(row, col)

            nextPos = moveToNext(row, col)

            if board[row][col] == '.':
                available_row = nums - set([num for num in board[row]])
                available_col = nums - set([num[col] for num in board])

                available_sub = nums - set([board[i][j] for i in getSubGroupRange(row)
                                            for j in getSubGroupRange(col)])
                candidate = list(available_row & available_col & available_sub)

                if not candidate:
                    return False

                for can in candidate:
                    # print(can)
                    board[row][col] = can
                    # print(board[row])
                    backtrack(nextPos[0], nextPos[1])
                    board[row][col] = '.'

            else:
                backtrack(nextPos[0], nextPos[1])

        res = []

        backtrack(0, 0)

        for row in range(n):
            for col in range(n):
                board[row][col] = res[row][col]


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]


]


so = Solution()


so.solveSudoku(board)


for row in board:
    print(row)

# def getSubGroupRange(idx: int):
#     if idx >= 6:
#         return [6, 7, 8]
#     elif idx >= 3:
#         return [3, 4, 5]
#     else:
#         return [0, 1, 2]


# x = 0
# y = 2

# nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
# row = nums - set([num for num in board[x]])
# col = nums - set([num[y] for num in board])

# sub = nums - set([board[i][j] for i in getSubGroupRange(x)
#                   for j in getSubGroupRange(y)])


# print(row)
# print(col)
# print(sub)


# print(row & col & sub)
