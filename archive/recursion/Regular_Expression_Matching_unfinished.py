# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.


from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        patterns = self.pattern_list(p)

        print(patterns)

        def dfs(start: int, s: str, patterns: List[str], p_idx: int) -> bool:
            # base
            # all characters and all patterns are processed
            if start == len(s) and p_idx == len(patterns):
                return True
            elif start == len(s) or p_idx == len(patterns):
                return False

            # match

            cur_result = None

            cur_p = patterns[p_idx]
            if len(cur_p) == 1 and cur_p != '.':
                cur_result = True if cur_p == s[start] else False
                return cur_result and dfs(start+1, s, patterns, p_idx+1)
            elif cur_p == '.':
                return dfs(start+1, s, patterns, p_idx+1)
            elif cur_p == '.*':
                # two cases
                #   1. match

                #   2. not match
                pass
            else:
                # 'c*'
                c = s[start]

                for i in range(start+1, len(s)):
                    if s[i] != c:
                        break
                return c == cur_p[0] and dfs(i, s, patterns, p_idx+1)

                # match current string

        return dfs(0, s, patterns, 0)

    def pattern_list(self, p: str) -> List[str]:

        res = []

        for i in range(len(p)):
            if p[i] in '*':
                res[-1] += p[i]
            else:
                res.append(p[i])
        return res


so = Solution()

s = 'aa'
# p = 'a*'
p = 'a'
#p = "c*a*b"
#p = ".*"
res = so.isMatch(s, p)

print(res)
