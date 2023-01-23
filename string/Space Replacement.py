'''
212 · Space Replacement
' ' -> %20

1. use new space


2. in place
 - 1 empty space -> 3 spaces =>  og len + n * 2
 - count how many empty spaces
 - looping backwards
 - 时间复杂度O(n),空间复杂度O(1)

'''

from typing import List


class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """

    def replaceBlank(self, string: List[str], length: int):
        # write your code here
        cnt = 0
        for i in range(length):
            if string[i] == ' ':
                cnt += 2

        j = length + cnt - 1

        # looping backwards
        for i in range(length-1, -1, -1):
            char = string[i]
            if char != ' ':
                string[j] = char
                j -= 1
            else:
                string[j] = '0'
                string[j-1] = '2'
                string[j-2] = '%'
                j -= 3

        return length + cnt


so = Solution()

# Mr John Smith
string = ['M', 'r', ' ', 'J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
length = 13

res = so.replaceBlank(string, length)
print(res)
print(string)
