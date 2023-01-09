

#  ()[]{}

# using stack
# ! count does not work since the relative position for different kind o brackets matters

# Time O(n)
# space O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        #! optimzied merge left and match
        left = '([{'
        stack = []
        match = {'()', '[]', '{}'}

        for bracket in s:
            if bracket in left:
                stack.append(bracket)
            else:
                if not stack:
                    return False

                val = stack.pop() + bracket

                if val not in match:
                    return False

        return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'}': '{', ')': '(', ']': '['}

        for bracket in s:
            if bracket in match:
                top_elemnt = stack.pop() if stack else '#'

                if match[bracket] != top_elemnt:
                    return False
            else:
                stack.append(bracket)

        return not stack


so = Solution()
s = "()"
s = "()[]{}"
s = "(]"
s = "([)]"
res = so.isValid(s)


print(res)
