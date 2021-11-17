from typing import List
from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ans_dict = defaultdict(list)

        for s in strings:
            l = []
            for c in s:
                l.append(ord(c) - ord('a'))

            # normalize
            first_val = l[0]

            for i, val in enumerate(l):
                l[i] = (l[i] - first_val) % 26

 #           print(l)

            ans_dict[tuple(l)].append(s)

        return ans_dict.values()


so = Solution()

strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

res = so.groupStrings(strings)


print(res)
