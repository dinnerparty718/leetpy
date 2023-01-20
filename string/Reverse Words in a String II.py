'''
927 · Reverse Words in a String II

#! reverse an arry a[::-1]

'''


from typing import List


class Solution:
    """
    @param str: a string
    @return: return a string
    """

    def reverse_words(self, s: str) -> str:

        def reverse(s: List[str], start: int, end: int):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        array = list(s)

        reverse(array, 0, len(array) - 1)

        start = 0
        for end in range(len(array)):
            if array[end] == ' ':
                reverse(array, start, end - 1)
                start = end + 1

        reverse(array, start, len(array)-1)
        return ''.join(array)


so = Solution()
s = 'the sky is blue'
res = so.reverse_words(s)
print(res)
