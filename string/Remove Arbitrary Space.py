'''
686 · Remove Arbitrary Space

if begining/ending is space, remove space

'''


class Solution:
    """
    @param s: the original string
    @return: the string without arbitrary spaces
    """

    def remove_extra(self, s: str) -> str:
        # write your code here
        res = ''
        i = 0

        while i < len(s):
            if s[i] == ' ':
                isntBegin = i != 0  # ! store the value first before increment i

                while i < len(s) and s[i] == ' ':
                    i += 1
                if isntBegin and i < len(s):
                    res += ' '

            while i < len(s) and s[i] != ' ':
                res += s[i]
                i += 1

        return res


class Solution2:
    """
    @param s: the original string
    @return: the string without arbitrary spaces
    """

    def remove_extra(self, s: str) -> str:
        return ' '.join(s.split())


so = Solution()
s = 'The  sky   is blue'
# s = '  low               ercase  '
res = so.remove_extra(s)
print(res, len(res))
