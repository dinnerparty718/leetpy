'''
209 · First Unique Character in a String
use hashmap

cnt = {}
char: index
a: 3
b: float('inf)
c: 1


min(cnt.value())


2. build [0] * 128

3. defaultdict set to 0

'''


from collections import defaultdict


class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def first_uniq_char(self, str: str) -> str:
        # Write your code here
        cnt = {}
        for i in range(len(str)):
            char = str[i]
            if char not in cnt:
                cnt[char] = i
            else:
                cnt[char] = float('inf')

        return str[min(cnt.values())] if min(cnt.values()) != float('inf') else ''


class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def first_uniq_char(self, str: str) -> str:
        # Write your code here
        cnt = [0] * 256

        for i in range(len(str)):
            cnt[ord(str[i])] += 1

        for i in range(len(str)):
            if cnt[ord(str[i])] == 1:
                return str[i]

        return ''


class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def first_uniq_char(self, str: str) -> str:
        # Write your code here
        counter = defaultdict(int)

        for i in range(len(str)):
            char = str[i]
            counter[char] += 1

        for i in range(len(str)):
            char = str[i]
            if counter[char] == 1:
                return char
        return ''


so = Solution()
str = 'abaccdeff'
res = so.first_uniq_char(str)
print(res)
