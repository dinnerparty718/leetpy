# Own
# Time O(n)
# Space O(1)
# ! since only lower letter char , 26
import collections


class Solution:
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


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)

        for i in range(len(s)):
            char = s[i]
            if cnt[char] == 1:
                return i
        return -1


so = Solution()

s = "leetcode"
s = "loveleetcode"
s = "aabb"

res = so.firstUniqChar(s)

print(res)
