

# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/1771657/A-simple-O(n)-approach

'''

                      -1 [0,  1,  2,  3,  4,  5,  6, 7] 8
                         L    E  E   T   C   O   D  E
                        [-1, -1, 1, -1, -1, -1, -1, 2]
                        [ 8,  2, 7,  8,  8,  8,  8, 8]
92


...A...A.....A.

...left * right


using hash map
left - right
find left boundary

right - left
right boundary

res += (i - left) * (right - i) 

ABC -> substring include B  left boundary -1 right boundary 3     

AB
B
ABC
BC


'''


import bisect


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        res = 0

        l = [-1] * n  # left boundary
        r = [n] * n  # right boundary

        alpha = {}

        for i in range(n):
            char = s[i]
            if char in alpha:
                l[i] = alpha[char]
            alpha[char] = i

        alpha = {}

        for i in range(n-1, -1, -1):
            char = s[i]
            if char in alpha:
                r[i] = alpha[char]
            alpha[char] = i

        for i in range(n):
            left_cnt = i - l[i]
            right_cnt = r[i] - i

            res += left_cnt * right_cnt

        # print(l)
        # print(r)

        return res


class Solution1:
    def uniqueLetterString(self, s: str) -> int:
        pimap = {}
        n = len(s)
        l = [0]*n
        r = [0]*n
        for i, ch in enumerate(s):
            if (ch in pimap):
                l[i] = i-pimap[ch]-1
            else:
                l[i] = i
            pimap[ch] = i
        pimap = {}
        i = n-1
        while (i >= 0):
            ch = s[i]
            if (s[i] in pimap):
                r[i] = pimap[ch]-i-1
            else:
                r[i] = n-i-1
            pimap[ch] = i
            i -= 1
        cnt = 0

        for i in range(n):
            cnt += (l[i]+1)*(r[i]+1)
        return cnt


# s = "LEETCODE"
s = "zzzyz"

so = Solution()

res = so.uniqueLetterString(s)

print(res)


bisect.bisect_right
