from collections import Counter, defaultdict


# own soltuion
# same as anagram

# https://leetcode.com/problems/permutation-in-string/solution/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        counter = Counter(s1)
        p_counter = defaultdict(int)
        n = len(s1)

        left = 0
        right = 0

        while right < len(s2):
            cur_char = s2[right]
            if cur_char not in counter:
                right += 1
                left = right

                p_counter = defaultdict(int)
            else:
                p_counter[cur_char] += 1

                if right - left + 1 == n:
                    if counter == p_counter:  # ! check if two hashmap equals
                        return True
                    else:
                        left_char = s2[left]
                        left += 1
                        p_counter[left_char] -= 1

                right += 1

        return False


so = Solution()

# s1 = "ab"
# s2 = "eidbaooo"

s1 = "adc"
s2 = "dcda"
s1 = "abc"
s2 = "bbbca"

res = so.checkInclusion(s1, s2)


print(res)
