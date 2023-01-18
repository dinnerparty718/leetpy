'''
Given a string, determine if a permutation of the string could form a palindrome.

2,2,2
2,2,1

# todo check bitmap https://www.lintcode.com/problem/916/solution/27548?fromId=297&_from=collection

Time O(n)
space O(1)


'''


class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """

    def can_permute_palindrome(self, s: str) -> bool:
        # write your code here
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        odd = 0

        for count in cnt:
            if count % 2 == 1:
                odd += 1
        return True if odd <= 1 else False


so = Solution()

s = 'carerac'

s = 'code'

res = so.can_permute_palindrome(s)
print(res)
