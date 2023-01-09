
# own two pointer with hash

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not haystack:
            return -1
        if needle == '':
            return 0

        needle_h = {}

        for nee in needle:
            needle_h[nee] = needle_h.get(nee, 0) + 1

        left = 0

        size = len(needle)

        haystack_h = {}

        for i in range(len(haystack)):
            char = haystack[i]

            haystack_h[char] = haystack_h.get(char, 0) + 1
            if haystack_h == needle_h and haystack[left:i+1] == needle:
                return left

            if i - left + 1 == size:
                remove_char = haystack[left]
                haystack_h[remove_char] -= 1

                if haystack_h[remove_char] == 0:
                    del haystack_h[remove_char]

                left += 1

        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1


haystack = "hello"
needle = "ll"


so = Solution()

res = so.strStr(haystack, needle)


print(res)
