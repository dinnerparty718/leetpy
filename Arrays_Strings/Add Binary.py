class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        ans = []

        for i in reversed(range(n)):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            if carry % 2 == 1:
                ans.append('1')
            else:
                ans.append('0')

            carry = carry // 2

        if carry == 1:
            ans.append('1')

        ans.reverse()

        return ''.join(ans)


so = Solution()
a = "11"
b = "1"
res = so.addBinary(a, b)
