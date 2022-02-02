from collections import Counter


# palindromes has 0 or 1 unpair chars

# own

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        even_len = len(s) % 2 == 0
        counter = Counter(s)

        if even_len:
            for v in counter.values():
                if v % 2 != 0:
                    return False
            return True
        else:
            odd_char_cnt = 0
            for v in counter.values():
                if v % 2 == 1:
                    odd_char_cnt += 1

            if odd_char_cnt == 1:
                return True
            else:
                return False


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        unpaired = set()

        for char in s:
            if char not in unpaired:
                unpaired.add(char)
            else:
                unpaired.remove(char)

        return len(unpaired) <= 1


so = Solution()

s = 'aab'

res = so.canPermutePalindrome(s)

print(res)
