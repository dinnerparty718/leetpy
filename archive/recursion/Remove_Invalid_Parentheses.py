from typing import List


# 1 Check whether a input strinig is valid
# count   ) < (  , i < n-1
# count   ) == (    i = n -1

# 2 comput miin number of ( and ) to remove unbalanced ) + unbalaned (
#    l = 0 , r = 1

# 3 try all possible ways to remove ) and (
#
# dfs(s, l, r):
#    if l == 0 and r == 0 and valid(s)
#         ans.add(s)

# to avoid duplicate
# only remove the first pransethesis if there are consecutive ones  ((

# time O (2 ^ (l + r))
# space O(n^2)


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # calculate l and r
        l, r = 0, 0

        for c in s:
            if c == '(':
                l += 1
            if c == ')':
                if l == 0:
                    r += 1  # 落单的右括号
                else:
                    l -= 1

        # print(l, r)

        ans = []

        def dfs(cur: str, start: int, l: int, r: int, ans: List[str]):
            if l == r == 0:
                if self.isValid(cur):
                    ans.append(cur if cur else '')
                return

            for i in range(start, len(cur)):

                if i != start and cur[i-1] == cur[i]:
                    continue

                if cur[i] in '()':
                    newCur = cur[:i] + cur[i+1:]
                    if r > 0:
                        dfs(newCur, i, l, r-1, ans)
                    else:
                        dfs(newCur, i, l-1, r, ans)

                # if cur[i] == ')' and r > 0:
                #     newCur = cur[:i] + cur[i+1:]
                #     dfs(newCur, i, l, r-1, ans)
                # elif cur[i] == '(' and l > 0 and r == 0:
                #     # remove '('
                #     newCur = cur[:i] + cur[i+1:]
                #     dfs(newCur, i, l-1, r, ans)

        dfs(s, 0, l, r, ans)
        return ans

    # empty '' is valid too

    def isValid(self, s: str) -> bool:
        l, r = 0, 0
        for c in s:
            if c == '(':
                l += 1
            if c == ')':
                r += 1

            # and any time in the loop, if count of ) greater than count of (, invalid
            if r > l:
                return False

        return l == r


s = "()())()"
#s = ")("


so = Solution()


res = so.removeInvalidParentheses(s)

print(res)
