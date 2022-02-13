
# Time O(m + n)
# Space O(n)

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0

        t_map = Counter(t)

        s_map = {key: 0 for key in t_map.keys()}

        ans = [float('inf'), None, None]

        #! can't be s_map == t_map
        #! values count can be higher

        while r < len(s):
            char = s[r]
            if char in s_map:
                s_map[char] += 1

            #! l <= r   length == 1
            while l <= r and all(v >= t_map[k] for k, v in s_map.items()):

                if r-l + 1 < ans[0]:
                    ans = [r-l + 1, l, r]

                l_char = s[l]

                if l_char in s_map:
                    s_map[l_char] -= 1

                l += 1

            r += 1

        return s[ans[1]: ans[2]+1] if ans[0] != float('inf') else ''


        # move l to check if smaller acount
s = "ADOBECODEBANC"
t = "ABC"

s = "a"
t = "a"

so = Solution()

res = so.minWindow(s, t)

print(res)
