from typing import List


# 3 * 3

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9

        def isValidMove(row: int, col: int, candidate: str):
            # check row
            if any(board[i][col] == candidate for i in range(9)):
                return False
            # check col

            if any(board[row][j] == candidate for j in range(9)):
                return False

            # check block
            br, bc = 3*(row//3), 3 * (col//3)

            if any(board[i][j] == candidate for i in range(br, br+3) for j in range(bc, bc+3)):
                return False

            return True

        def backtrack(i: int, j: int):
            # Go to next empty space
            while board[i][j] != '.':
                if j == n-1:
                    i = i+1
                    j = 0
                else:
                    j += 1

                if i == n:
                    return True  # trick

            for k in range(1, 10):
                if isValidMove(i, j, str(k)):
                    board[i][j] = str(k)
                    if backtrack(i, j):
                        return True
            board[i][j] = '.'
            return False

        backtrack(0, 0)


# own improved
class Solution1:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = 9

        nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        # def getSubGroup(i: int, j: int):
        #     return (i // 3) + (j // 3) * 3

        def getSubGroupRange(idx: int):
            if idx >= 6:
                return [6, 7, 8]
            elif idx >= 3:
                return [3, 4, 5]
            else:
                return [0, 1, 2]

        def backtrack(row: int, col: int):
            while board[row][col] != '.':
                if col == n-1:
                    row += 1
                    col = 0
                else:
                    col += 1

                if row == n:
                    return True

            available_row = nums - set([num for num in board[row]])
            available_col = nums - set([num[col] for num in board])
            available_sub = nums - set([board[i][j] for i in getSubGroupRange(row)
                                        for j in getSubGroupRange(col)])
            candidate = list(available_row & available_col & available_sub)

            if not candidate:
                return False

            for can in candidate:
                board[row][col] = can
                if backtrack(row, col):
                    return True

            board[row][col] = '.'
            return False

        backtrack(0, 0)


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


so = Solution1()


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
