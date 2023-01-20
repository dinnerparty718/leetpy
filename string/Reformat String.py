'''
315 · Reformat String
start by 1 and skip eac time   1, 3, 5, 7

Time O(n) O(str.length())
Space O(n)

'''


from typing import (
    List,
)


class Solution:
    """
    @param str: the original string
    @param sublen: an integer array
    @return: the new string
    """

    def reformat_string(self, str: str, sublen: List[int]) -> str:
        # write your code here
        res = ''
        n = len(sublen)
        j = 0
        for i in range(1, n, 2):
            res = res + str[j + sublen[i-1]: j + sublen[i-1] + sublen[i]] + str[j: j + sublen[i-1]]
            j += sublen[i-1] + sublen[i]

        if n % 2 == 1:
            res += str[j: j + sublen[n-1]]

        return res


so = Solution()

s = 'abcdefghi'
sublen = [3, 2, 2, 1, 1]

res = so.reformat_string(s, sublen)
print(res)
