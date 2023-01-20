'''
78 · Longest Common Prefix

LCP
neetcoce
https://www.youtube.com/watch?v=0sWShKIJoo4


Time: O(mn) worse case
Space: O(1)

'''

from typing import (
    List,
)


class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """

    def longest_common_prefix(self, strs: List[str]) -> str:
        # write your code here
        res = ''

        if not strs:
            return res

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res


class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """

    def longest_common_prefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        length, count = len(strs[0]), len(strs)

        for i in range(length):
            c = strs[0][i]
            #! check out of bound
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]  # ! not including i

        return strs[0]  # the first string


so = Solution()

strs = ["ABCD", "ABEF", "ACEF"]

res = so.longest_common_prefix(strs)
print(res)
