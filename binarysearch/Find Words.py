'''
194 · Find Words

392 subsequence

'''


from typing import (List)


class Solution:
    """
    @param str: the string
    @param dict: the dictionary
    @return: return words which are subsequences of the string
    """

    def find_words(self, str: str, dict: List[str]) -> List[str]:
        # write your code here.
        pass

    def get_next_positions(self, s):
        next_positions = {
            i: {j: -1 for j in 'abcdefghijklmnopqrstuvwxyz'}
            for i in range(len(s) + 1)
        }
        last_positions = {
            i: -1 for i in 'abcdefghijklmnopqrstuvwxyz'
        }

        for i in range(len(s)-1, -1, -1):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_positions[i + 1][char]


str = "bcogtadsjofisdhklasdj"
dict = ["book", "code", "tag"]


s = Solution()
s.get_next_positions('b')
