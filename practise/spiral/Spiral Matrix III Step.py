from typing import List


# step 1,1,2,2,3,3,4,4,5,5,6,6,

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        def isValid(row: int, col: int) -> bool:
            if 0 <= row < rows and 0 <= col < cols:
                return True
            else:
                return False

        output = [[rStart, cStart]]

        row = rStart
        col = cStart

        step = 1

        N = 1  # ! start from 1, otherwise will end if in infinit loop

        while N < rows * cols:

            # top left -> right

            for _ in range(step):
                col += 1
                if isValid(row, col):
                    output.append([row, col])
                    N += 1
            # right top -> Bottom
            for _ in range(step):
                row += 1
                if isValid(row, col):
                    output.append([row, col])
                    N += 1

            step += 1

            # bototm right -> left
            for _ in range(step):
                col -= 1
                if isValid(row, col):
                    output.append([row, col])
                    N += 1

            # left bottom -> top

            for _ in range(step):
                row -= 1
                if isValid(row, col):
                    output.append([row, col])
                    N += 1

            step += 1

        return output


so = Solution()

rows = 5
cols = 6
rStart = 1
cStart = 4
res = so.spiralMatrixIII(rows, cols, rStart, cStart)

print(res)
