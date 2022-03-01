# Own
# Time O(n)
# Space O(1)
# ! since only lower letter char , 26


'''
counter = [0] * 26

one pass for counter

second pass to return the first letter when cnt = 1


'''


import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = [0] * 128

        for char in s:
            idx = ord(char)
            counter[idx] += 1

        for i, char in enumerate(s):
            idx = ord(char)
            if counter[idx] == 1:
                return i
        return -1


class Solution2:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)

        for i in range(len(s)):
            char = s[i]
            if cnt[char] == 1:
                return i
        return -1


class Solution3:
    def firstUniqChar(self, s: str) -> int:
        cnt = {}
        MAX = float('inf')

        for i in range(len(s)):
            char = s[i]
            if char not in cnt:
                cnt[char] = i
            else:
                cnt[char] = MAX
        #! python min max time complexicty O(n)
        return min(cnt.values()) if min(cnt.values()) != MAX else -1


so = Solution()

s = "leetcode"
# s = "loveleetcode"
# s = "aabb"

res = so.firstUniqChar(s)

print(res)
