from typing import List


# own solution
# one hash set
# time O(n^2)
# space O(n^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h_list = set()
        N = 9
        # key (block_i, block_j, value)

        for i in range(N):
            for j in range(N):
                block_i = int(i / 3)
                block_j = int(j / 3)

                val = board[i][j]

                if val == '.':
                    continue

                if (block_i, block_j, val) in h_list:
                    return False
                else:
                    h_list.add((block_i, block_j, val))

                if ('row', i, val) in h_list:
                    return False
                else:
                    h_list.add(('row', i, val))

                if ('col', j, val) in h_list:
                    return False
                else:
                    h_list.add(('col', j, val))

        return True


class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        row_s = set()
        col_s = set()
        box = set()

        for i in range(N):
            for j in range(N):
                block_i = int(i / 3)
                block_j = int(j / 3)

                val = board[i][j]

                if val == '.':
                    continue

                if (block_i, block_j, val) in box:
                    return False
                else:
                    box.add((block_i, block_j, val))

                if (i, val) in row_s:
                    return False
                else:
                    row_s.add((i, val))

                if (j, val) in col_s:
                    return False
                else:
                    col_s.add((j, val))

        return True


class Solution3:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        #
        rows = [[0] * N for _ in range(N)]
        cols = [[0] * N for _ in range(N)]
        boxes = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if board[r][c] == '.':
                    continue
                # number to index
                pos = int(board[r][c]) - 1

                if rows[r][pos] == 1:
                    return False
                rows[r][pos] = 1

                if cols[c][pos] == 1:
                    return False
                cols[c][pos] = 1

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if boxes[idx][pos] == 1:
                    return False
                boxes[idx][pos] = 1

        return True


so = Solution()

board = [
    [".", ".", "4", ".", ".", ".", "6", "3", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", "9", "."],
    [".", ".", ".", "5", "6", ".", ".", ".", "."],
    ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
    [".", ".", ".", "7", ".", ".", ".", ".", "."],
    [".", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]
print(so.isValidSudoku(board))
