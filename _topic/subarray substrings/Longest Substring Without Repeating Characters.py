'''

asc a-z 97-123
    65 A
use hashmap or array [0] * 26  or [0]*128 to keep track of count

l = 0

for r in range(n):
    char = s[r]
    cnt[ord(char)] +=1
    
    while cnt[ord(char)] > 1
        # shrink left
        left = s[l]
        cnt[ord(left)] -=1
        left+=1
    
    
    update globbal max



'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #! does not need to care about shifting
        # will fit
        char = [0] * 128

        left = right = 0

        res = 0

        while right < len(s):
            r = s[right]
            char[ord(r)] += 1

            #! can't be duplicated
            while char[ord[r]] > 1:
                l = s[left]
                char[ord[l]] -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1

        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        mp = {}
        left = 0

        for right in range(n):
            if s[right] in mp:
                left = max(mp[s[right]], left)

            ans = max(ans, right - left + 1)
            mp[s[right]] = right + 1

        return ans

# two pointer optimized
# own


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = {}   # store    char:last_index

        l = r = 0

        max_len = 0

        while r < len(s):
            char = s[r]

            #! important
            if char not in cnt or cnt[char] < l:
                cnt[char] = r
                max_len = max(max_len, r - l + 1)

            else:
                l = cnt[char] + 1
                cnt[char] = r

            r += 1
        return max_len


s = "abcabcbb"
#s = "bbbbb"
#s = "pwwkew"


#s = "abba"


s = "tmmzuxt"

so = Solution()

res = so.lengthOfLongestSubstring(s)

print(res)
