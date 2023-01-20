'''
1169 · Permutation in String

sliding window(two pointer) compare counter to counter
l, r

#! python dict compare, it's comparing it's value regardless of the order

https://leetcode.com/problems/permutation-in-string/submissions/625225865/

'''

from collections import Counter, defaultdict


class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """

    def check_inclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        p_counter = defaultdict(int)

        n = len(s1)

        left, right = 0, 0

        while right < len(s2):
            cur_char = s2[right]
            if cur_char not in counter:
                right += 1
                left = right

                p_counter = defaultdict(int)  # reset
            else:
                p_counter[cur_char] += 1
                if right - left + 1 == n:
                    if counter == p_counter:
                        return True
                    else:
                        left_char = s2[left]
                        left += 1
                        p_counter[left_char] -= 1
            right += 1
        return False


so = Solution()

s1 = 'ab'
s2 = 'eidbaooo'
s2 = 'eidboaoo'
res = so.check_inclusion(s1, s2)
print(res)
