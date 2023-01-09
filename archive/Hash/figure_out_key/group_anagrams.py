from typing import List
from collections import defaultdict

# sort time NKlog(K)  K is the length of the string
# space O(KN)

'''

#todo

tuple([0]*26)



'''


# own
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def sortS(s: str):
            list1 = [c for c in s]
            list1.sort()
            return ''.join(list1)

        res_dict = defaultdict(list)
        for s in strs:
            res_dict[sortS(s)].append(s)

        return res_dict.values()


# better version using sorted()

#! sorted(s) returns a list of chars, which is mutable and unhashable, you need to convert it to a string.


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res_dict = defaultdict(list)
        for s in strs:
            res_dict[tuple(sorted(s))].append(s)

        return res_dict.values()


# even better
# time O(NK)
# space O(NK)

class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            res_dict[tuple(count)].append(s)

        return res_dict.values()


so = Solution2()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

res = so.groupAnagrams(strs)
print(res)
