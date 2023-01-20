'''
171 · Anagrams
use [0] * 26
can sort and put in hashmap

time O(n)
space O(n)

leetcode 49. Group Anagrams
https://leetcode.com/problems/group-anagrams/description/

'''


from typing import (
    List,
)

from collections import defaultdict


class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
             we will sort your return value in output
    """

    def anagrams(self, strs: List[str]) -> List[str]:
        # write your code here
        h = defaultdict(list)

        res = []

        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            h[tuple(count)].append(string)

        for items in h.values():
            if len(items) > 1:
                res += items

        return res


so = Solution()

strs = ["lint", "intl", "inlt", "code"]
strs = ["ab", "ba", "cd", "dc", "e"]
res = so.anagrams(strs)
print(res)
