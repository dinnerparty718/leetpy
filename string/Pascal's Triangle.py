'''
        n
1       1
11      2
1 2  1  3
1 3 3 1 4

  
'''


from typing import (
    List,
)


class Solution:
    """
    @param num_rows: num of rows
    @return: generate Pascal's triangle
    """

    def generate(self, num_rows: int) -> List[List[int]]:
        # write your code here
        res = []

        for i in range(num_rows):
            row = []
            for j in range(0, i + 1):
                if j == 0 or j == i:  # ! first and last is 1
                    row.append(1)
                else:
                    row.append(res[-1][j] + res[-1][j-1])

            res.append(row)

        return res


so = Solution()
num_rows = 5
res = so.generate(num_rows)
print(res)
