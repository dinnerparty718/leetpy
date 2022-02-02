

# 8 0 1


# 6 -> 9
# 9 -> 6

# own two pointer


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        if not num:
            return True

        mirror = {
            '8': '8',
            '0': '0',
            '6': '9',
            '9': '6',
            '1': '1'
        }
        l, r = 0, len(num)-1
        while l < r:

            if num[l] not in mirror or num[r] not in mirror:
                return False

            if mirror[num[l]] != num[r]:
                return False

            l += 1
            r -= 1

        if l == r:
            if num[l] not in '801':
                return False

        return True


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mirror = {
            '8': '8',
            '0': '0',
            '6': '9',
            '9': '6',
            '1': '1'
        }

        l, r = 0, len(num)-1

        while l <= r:
            if num[l] not in mirror or mirror[num[l]] != num[r]:
                return False
            l += 1
            r -= 1

        return True


so = Solution()
num = "868"

res = so.isStrobogrammatic(num)

print(res)
