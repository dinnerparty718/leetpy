from collections import Counter

# palindrome has 0 or 1 unpairs
# own
# time O(N)
# space O(1)


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c_map = Counter(s)

        pair_cnt = 0
        unpair_cnt = 0

        for key, count in c_map.items():
            if count >= 2:
                c_map[key] = count % 2
                pair_cnt += (count // 2)*2

                if c_map[key] == 1 and unpair_cnt == 0:

                    unpair_cnt = 1
            else:
                if unpair_cnt == 0:
                    unpair_cnt = 1

        return pair_cnt + unpair_cnt


class Solution:
    def longestPalindrome(self, s: str) -> int:

        pairs = 0
        unpaired_chars = set()

        for c in s:
            if c in unpaired_chars:
                unpaired_chars.remove(c)
                pairs += 1
            else:
                unpaired_chars.add(c)

        if unpaired_chars:
            return pairs * 2 + 1
        else:
            return pairs * 2


so = Solution()

s = 'bb'

res = so.longestPalindrome(s)

print(res)
