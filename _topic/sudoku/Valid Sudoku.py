from typing import List

'''

sub box

(i // 3) * 3 + j // 3




'''
# time O(n^2)
# space O(n^2)


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        #! store tuples
        row_s = set()  # (i, val)
        col_s = set()  # (j, val)
        box = set()  # (i,j, val)

        for i in range(n):
            for j in range(n):

                val = board[i][j]
                block_i = i // 3
                block_j = j // 3

                if val == '.':
                    continue

                #! validate box

                if (block_i, block_j, val) in box:
                    return False
                else:
                    box.add((block_i, block_j, val))

                #! row
                if (i, val) in row_s:
                    return False
                else:
                    row_s.add((i, val))

                #! col
                if (j, val) in col_s:
                    return False
                else:
                    col_s.add((j, val))

        return True


so = Solution()


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

res = so.isValidSudoku(board)

print(res)
