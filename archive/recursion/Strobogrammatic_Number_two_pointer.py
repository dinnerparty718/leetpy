# 0,1,8
# 6->9

# own time O(n)
#     space O(1)
# two pointer approint
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        m = {
            '0': '0',
            '1': '1',
            '8': '8',
            '6': '9',
            '9': '6'
        }

        l = 0
        r = len(num)-1

        while l <= r:

            if num[l] not in m and num[r] not in m:
                return False

            if m[num[l]] != num[r]:
                return False

            l += 1
            r -= 1

        # if l == r:
        #     if num[l] not in m:
        #         return False
        #     else:
        #         return m[num[l]] == num[l]
        # else:
        return True


class Solution2:
    def isStrobogrammatic(self, num: str) -> bool:

        m = {
            '0': '0',
            '1': '1',
            '8': '8',
            '6': '9',
            '9': '6'
        }

        # build rotated string
        s = ''

        # for i in reversed(range(len(num))):

        for i in range(len(num)-1, -1, -1):
            if num[i] in m:
                s += m[num[i]]
            else:
                return False

        return s == num


so = Solution()
num = '639'
res = so.isStrobogrammatic(num)
print(res)
