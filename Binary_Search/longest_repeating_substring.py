# solution1 brute force
# hashset O(n) * find substring O(n^2) total O(n^3)
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        count = 0

        # len of substring, staring from 1
        for n in range(1, len(s)):
            seen = set()
            for i in range(len(s) - n + 1):
                sub = s[i:i + n]
                if sub in seen:
                    count += 1
                    break
                else:
                    seen.add(sub)

        return count


# binary search [0, n)   does not inlucde oringal length
class Solution2:
    def longestRepeatingSubstring(self, s: str) -> int:
        l = 0
        r = len(s)-1

        while l < r:
            mid = l + (r - l + 1) // 2
            # if exist n that have repeated n length substring, preserse that value
            if self.f(s, mid):
                l = mid
            else:
                r = mid-1

        return l

    def f(self, s, n) -> bool:
        seen = set()
        for i in range(len(s) - n + 1):
            sub = s[i:i+n]
            if sub in seen:
                return True
            else:
                seen.add(sub)

        return False


so = Solution2()


s = 'abbaba'

res = so.longestRepeatingSubstring(s)


print(res)
