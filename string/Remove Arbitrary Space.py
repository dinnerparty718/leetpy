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
            while s[i] == ' ':
                i += 1
            if i >= len(s):
                break
            if res:
                res += f' {s[i]}'
            else:
                res += s[i]
            i += 1

        return res


so = Solution()
s = 'The  sky   is blue'
res = so.remove_extra(s)
print(res)
