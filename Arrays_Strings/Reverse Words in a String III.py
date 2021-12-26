class Solution:
    def reverseWords(self, s: str) -> str:

        l = s.split()

        def reverse(s: str) -> str:

            l = []

            for i in reversed(range(len(s))):
                l.append(s[i])

            return ''.join(l)

        res = []

        for w in l:
            res.append(reverse(w))

        return (' ').join(res)


# two pointer without split
# no leading/trailing only one space in between
class Solution1:
    def reverseWords(self, s: str) -> str:
        start = end = 0
        n = len(s)

        res = []

        while start < n:
            while end < n and s[end] != ' ':
                end += 1

            # s[end] == ' '
            word = [w for w in s[start: end]]

            l = 0
            r = len(word)-1
            while l < r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1

            res.append(''.join(word))

            start = end + 1
            end += 1

        return ' '.join(res)


so = Solution1()


s = "Let's take LeetCode contest"


res = so.reverseWords(s)


print(res)
