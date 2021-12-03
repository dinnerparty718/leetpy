from collections import defaultdict
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''

        dict_t = Counter(t)

        required = len(dict_t)
        have = 0

        l, r = 0, 0

        # can hold all the character in the list
        window_counts = defaultdict(int)

        # ans tuple of the form (window lenght, left, right)
        ans = float('inf'), None, None

        for r in range(len(s)):
            c = s[r]

            window_counts[c] += 1

            if c in dict_t and window_counts[c] == dict_t[c]:
                have += 1

            while l <= r and have == required:
                # update result
                if (r-l + 1) < ans[0]:
                    ans = (r-l+1, l, r)

                c = s[l]

                window_counts[c] -= 1

                if c in dict_t and window_counts[c] < dict_t[c]:
                    have -= 1
                l += 1
        lenghth, l, r = ans

        return "" if lenghth == float('inf') else s[l: r+1]


so = Solution()

s = 'ADOBECODEBANC'
t = 'ABC'
res = so.minWindow(s, t)

print(res)
