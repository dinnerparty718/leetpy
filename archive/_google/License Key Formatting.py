class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        S = s.upper().replace('-', '')

        size = len(S)

        s1 = k if size % k == 0 else size % k
        res = S[:s1]

        while s1 < size:
            res += '-' + S[s1: s1+k]
            s1 += k
        return res


so = Solution()


s = "5F3Z-2e-9-w"
k = 4

res = so.licenseKeyFormatting(s, k)

print(res)
