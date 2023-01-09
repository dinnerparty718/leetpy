
# valid  current windows length - most common  < k
# all upper case, 26


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        left = right = 0

        res = 0

        most_common = 0

        while right < len(s):
            char = s[right]
            cnt[char] = cnt.get(char, 0) + 1

            most_common = max(most_common, cnt[char])

            # if right - left + 1 - most_common <= k:

            while right - left + 1 - most_common > k:
                cnt[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

            right += 1

        return res


so = Solution()
s = "ABAB"
k = 2

res = so.characterReplacement(s, k)
print(res)
