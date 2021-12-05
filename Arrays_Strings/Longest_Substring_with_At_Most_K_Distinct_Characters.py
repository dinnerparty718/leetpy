from collections import defaultdict

# own solution
# Sliding window + hashmap
# Time O(n)


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = defaultdict(int)
        l = 0
        max_len = float('-inf')

        for r in range(len(s)):
            c = s[r]
            d[c] += 1

            if len(d) <= k:
                max_len = max(max_len, r - l + 1)

            while len(d) > k:
                # shrink left
                c = s[l]

                d[c] -= 1

                # delete the key
                if d[c] == 0:
                    del d[c]
                l += 1

        return max_len if max_len != float('-inf') else 0


so = Solution()

s = 'aa'
k = 1
res = so.lengthOfLongestSubstringKDistinct(s, k)

print(res)
