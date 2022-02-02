# own second time
# try skipping from left side
# try skipping from right side if prev result is False
class Solution:
    def validPalindrome(self, s: str) -> bool:

        l, r = 0, len(s)-1
        skip = False

        # skip left

        left_result = True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif skip == False:
                # skip left
                l += 1
                skip = True

            else:
                left_result = False
                break

        if left_result:

            return True

        right_result = True

        l, r = 0, len(s)-1
        skip = False

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif skip == False:
                # skip right
                r -= 1
                skip = True
            else:
                right_result = False
                break

        return right_result


s = "aba"

so = Solution()

res = so.validPalindrome(s)

print(res)
