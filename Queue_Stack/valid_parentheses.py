from collections import deque

# time space O(n)


class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False

        left = set(['(', '[', '{'])
        right = set([')', ']', '}'])
        match = [('(', ')'), ('[', ']'), ('{', '}')]

        if s[0] in right:
            return False

        stack = deque()

        # for i in range(len(s)):
        #     if s[i] in left:
        #         stack.append(s[i])
        #     else:
        #         if not stack:
        #             return False
        #         else:
        #             pair = (stack.pop(), s[i])
        #             if pair not in match:
        #                 return False

        for c in s:
            if c in left:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    if (stack.pop(), c) not in match:
                        return False
        return not stack


solution = Solution()

input = "(){}}{"


res = solution.isValid(input)


print(res)
