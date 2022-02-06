from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        mapping = [0, 1, 'abc', 'edf', 'ghi',
                   'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        res = []

        def backtrack(index: int, curr: List[str]):

            if index == len(digits):
                res.append(''.join(curr[:]))
                return

            digit = int(digits[index])

            for nxt in mapping[digit]:
                curr.append(nxt)
                backtrack(index+1, curr)
                curr.pop()

        backtrack(0, [])
        return res


so = Solution()

digits = "23"
digits = ''
digits = "2"
res = so.letterCombinations(digits)

print(res)
