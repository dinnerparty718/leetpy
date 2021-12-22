from typing import List

# back track, passing value down


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        com = [0, 1, 'abc', 'edf', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        if not digits:
            return []

        res = []

        def dfs(cur: List[str], i: int):
            # base case
            if i == len(digits):
                res.append(''.join(cur))
                return

            for c in com[int(digits[i])]:
                cur.append(c)
                dfs(cur, i+1)
                cur.pop()

        dfs([], 0)

        return res


digits = '23'

so = Solution()
res = so.letterCombinations(digits)


print(res)
