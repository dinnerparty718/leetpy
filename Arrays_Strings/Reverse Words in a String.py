from typing import List
import re


# own leetcode 2
# strim white space
# reverse the whole string
# reverse each worl

# use build function to trim
class Solution:
    def reverseWords(self, s: str) -> str:
        s = re.sub("\s+", " ", s.strip())
        lst = [' '] * len(s)

        j = 0

        for i in reversed(range(len(s))):
            lst[j] = s[i]
            j += 1

        def swap(i: int, j: int):
            while i < j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1

        left = 0

        print(lst)

        for right in range(len(lst)):
            if lst[right] == ' ':
                swap(left, right-1)
                left = right + 1

        swap(left, len(lst)-1)

        return ''.join(lst)


# space and time O(n)
# algo to trim white space
# and push to deque time/space O(n)
class Solution1:

    def trim_spaces(self, s: str):
        l, r = 0, len(s)-1
        # remove leading spaces

        while l <= r and s[l] == ' ':
            l += 1

        while l <= r and s[r] == ' ':
            r -= 1

        # reduce multiple space into sing one

        output = []

        while l <= r:
            if s[l] != ' ':
                output.append(s[l])
            elif output[-1] != ' ':  # use output and check last element
                output.append(s[l])  # only output one space

            l += 1
        return output

    def reverseList(self, l: list, left: int, right: int):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    def reverse_each_wrod(self, l: list):

        n = len(l)
        start = end = 0

        while start < n:
            # go to the end of the word
            while end < n and l[end] != ' ':
                end += 1

            # end stops at ' '
            self.reverseList(l, start, end-1)

            # move the the next word
            start = end+1
            end += 1

    def reverseWords(self, s: str):
        # convert string to char array
        # and trim spaces at the same time
        l = self.trim_spaces(s)

        # reverse the whold string
        self.reverseList(l, 0, len(l)-1)

        # reverse each word
        self.reverse_each_wrod(l)

        return ''.join(l)


# time,space O(n) # fast

class Solution2:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


so = Solution1()

s = "  hello  world  "


s = "a good   example"
res = so.reverseWords(s)


print(res)
