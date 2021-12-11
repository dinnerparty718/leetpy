from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == '':
            return []

        d_c_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        input = []

        for c in digits:
            input.append(d_c_map[c])

        def combine_two(l1: List[str], l2: List[str]) -> List[str]:
            com = []

            for c1 in l1:
                for c2 in l2:
                    com.append(c1 + c2)
            return com

        res = input[0]

        for i in range(1, len(input)):
            res = combine_two(res, input[i])

        return res


# back tracking
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAPPING = ('0', '1', 'abc', 'def', 'ghi',
                   'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')

        res = []

        def makeList(i, cur: List[str]):
            if i == len(digits):
                if len(cur) > 0:
                    res.append(''.join(cur))
                return

            for ch in MAPPING[int(digits[i])]:
                cur.append(ch)
                makeList(i+1, cur)
                cur.pop()

        makeList(0, [])

        return res


digits = '23'

so = Solution()
res = so.letterCombinations(digits)


print(res)
