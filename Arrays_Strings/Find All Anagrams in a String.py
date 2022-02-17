from typing import Dict, List
from collections import Counter


'''
# todo check solution
Sliding Window with HashMap
window size is fixed

s, t

early return if len(s) < len(t)

l = 0

t_counter = Counter(t)
s_counter = { key: 0 for key in t_counter.keys() }

res = []

for r in range(len(s)):
    if s[r] in s_counter:
        s_counter[key] +=1
        
    if r - l + 1 > len(t):
        if s[l] in s_counter:
            s_counter[key] -=1
        l+=1
        
    if s_counter == t_counter:
        res.append(l)
    


return res

'''


# own Yass!  sliding windows + hash table

# todo check leetcode solution

# Time( S + P)
# Space O(1)  26  * 2 is consider constant

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        cur = {}

        self.resetCurDict(cur, counter)

        left = 0
        right = 0

        res = []

        while right < len(s):
            char = s[right]

            if char not in counter:
                right += 1
                left = right

                self.resetCurDict(cur, counter)

            else:
                cur[char] += 1

                n = right - left + 1

                if n == len(p):
                    if self.isCurMatchCount(cur, counter):
                        res.append(left)
                    left_char = s[left]
                    cur[left_char] -= 1
                    left += 1

                right += 1

        return res

    def resetCurDict(self, cur: Dict, counter: Dict):
        for key in counter.keys():
            cur[key] = 0

    def isCurMatchCount(self, cur: Dict, counter: Dict):
        for key in counter.keys():
            if cur[key] != counter[key]:
                return False

        return True


s = "abab"
p = "ab"


so = Solution()

res = so.findAnagrams(s, p)

print(res)
