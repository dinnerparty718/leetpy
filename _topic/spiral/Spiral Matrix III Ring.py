from typing import List


# from leetcode discussion
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        i = rStart
        j = cStart

        left, right = cStart, cStart
        top, bottom = rStart, rStart

        result = [[i, j]]

        # until the ring is completely out of bound
        while top >= 0 or bottom < rows or left >= 0 or right < cols:
            j += 1  # step right into the next ring

            right += 1
            bottom += 1
            left -= 1
            top -= 1

            # walk the ring, go donw

            while i < bottom:
                if 0 <= i < rows and 0 <= j < cols:
                    result.append([i, j])
                i += 1

            # go left
            while j > left:
                if 0 <= i < rows and 0 <= j < cols:
                    result.append([i, j])
                j -= 1

            # go up
            while i > top:
                if 0 <= i < rows and 0 <= j < cols:
                    result.append([i, j])
                i -= 1

            # go right
            while j < right:
                if 0 <= i < rows and 0 <= j < cols:
                    result.append([i, j])
                j += 1

            # top right of the ring
            # !important
            # !draw graph
            if 0 <= i < rows and 0 <= j < cols:
                print(j, right)
                print('here', i, j)
                result.append([i, j])

        return result


so = Solution()

rows = 5
cols = 6
rStart = 1
cStart = 4
res = so.spiralMatrixIII(rows, cols, rStart, cStart)

print(res)
