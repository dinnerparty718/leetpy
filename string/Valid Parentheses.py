'''
stack

1. build dict ),].}
2. use stack

'''


class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """

    def is_valid_parentheses(self, s: str) -> bool:
        pairs = {'}': '{', ']': '[', ')': '('}
        stack = []

        for chr in s:
            if chr not in pairs:
                stack.append(chr)
            else:
                if not stack:
                    return False
                if pairs[chr] != stack.pop():
                    return False

        return not stack


so = Solution()
s = '([)]'
s = '()[]{}'
res = so.is_valid_parentheses(s)
print(res)
