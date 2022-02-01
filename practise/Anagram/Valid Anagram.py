from collections import Counter


# Time   O(n)
# space  O(n)


# hash table is best solution. can handle unicode
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        return c1 == c2

# if only 26 char  a-c
# Time   O(n)
# space  O(1)


# alternative #!  ord('a')- ord('a') = 0


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1

        return all(c == 0 for c in counter)


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         pass


so = Solution()

# s = "anagram"
# t = "nagaram"

# s = "rat"
# t = "car"

s = "a"
t = "ab"

res = so.isAnagram(s, t)


print(res)
