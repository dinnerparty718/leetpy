from collections import deque


# own solution using stack
# todo optimize it to use less stack
class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()

        for c in s:
            if c.isalnum() or c == '[':
                stack.append(c)
            else:  # ]
                tmp = deque()
                while stack and stack[-1] != '[':
                    tmp.appendleft(stack.pop())
                stack.pop()  # remove '['

                # get subsequent number

                numStr = deque()

                while stack and stack[-1].isnumeric():
                    numStr.appendleft(stack.pop())
                # n = stack.pop()  # a number
                stack.append(''.join(tmp) * int(''.join(numStr)))
        res = ''
        while stack:
            res += stack.popleft()
        return res


class Solution2:
    def decodeString(self, s: str) -> str:
        stack = deque()

        for c in s:
            if c != ']':
                stack.append(c)
            else:  # ]
                # tmp = deque()
                tmp_str = []
                while stack and stack[-1] != '[':
                    # tmp.appendleft(stack.pop())
                    tmp_str.append(stack.pop())

                stack.pop()  # remove '['

                # get subsequent number
                numStr = []
                while stack and stack[-1].isdigit():
                    numStr.append(stack.pop())
                # n = stack.pop()  # a number
                stack.append(''.join(reversed(tmp_str)) *
                             int(''.join(reversed(numStr))))
        res = ''
        while stack:
            res += stack.popleft()
        return res


# leetcode top vote python
# solution 3,4 similar approache work on currString until it sees a '['

class Solution3:
    def decodeString(self, s: str) -> str:
        stack = []
        currNum = 0
        currString = ''

        for c in s:
            if c == '[':
                stack.append(currString)
                stack.append(currNum)
                currString = ''
                currNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                currString = prevString + num * currString
            elif c.isdigit():
                currNum = currNum * 10 + int(c)
            else:
                currString += c
        return currString


# recursive
class Solution4:
    def decodeString(self, s: str) -> str:
        def dfs(s, p):
            res = ''
            i, num = p, 0
            while i < len(s):
                if s[i].isdigit():
                    num = num*10 + int(s[i])
                elif s[i] == '[':
                    local, pos = dfs(s, i+1)
                    res += local * num
                    i = pos
                    num = 0
                elif s[i] == ']':
                    return res, i
                else:
                    res += s[i]
                i += 1
            return res, i
        return dfs(s, 0)[0]


so = Solution4()

#s = "3[a]2[bc]"
s = "3[a2[c]]"
#s = '100[leetcode]'
res = so.decodeString(s)


print(res)
