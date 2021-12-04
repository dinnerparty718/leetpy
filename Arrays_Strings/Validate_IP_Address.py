
# time O(n)
# space O(1)
# divide and conquer
# own
# todo check regular expresssion
class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def check255(s: str) -> bool:
            # check if numeric

            if len(s) == 0:
                return False

            for c in s:
                if not c.isnumeric():
                    return False

            # check leading zero

            if len(s.lstrip('0')) != len(s) and len(s) != 1:
                return False
            return True if 0 <= int(s) <= 255 else False

        def checkHex(s: str):
            s = s.lower()

            if not (1 <= len(s) <= 4):
                return False

            for w in s:
                if w.isalpha() and w not in ['a', 'b', 'c', 'd', 'e', 'f']:
                    return False
            return True

        if not queryIP or ('.' in queryIP and ':' in queryIP):
            return 'Neither'

        if '.' in queryIP:
            arr = queryIP.split('.')

            if len(arr) == 4:
                for a in arr:
                    if not check255(a):
                        return 'Neither'

                return 'IPv4'
            else:
                return 'Neither'

        if ':' in queryIP:
            arr = queryIP.split(':')

            if len(arr) == 8:
                for a in arr:
                    if not checkHex(a):
                        return 'Neither'
                return 'IPv6'
            else:
                return 'Neither'


class Solution2:
    def validIPAddress(self, queryIP: str) -> str:

        if queryIP.count('.') == 3:
            return self.validate_IPV4(queryIP)
        elif queryIP.count(':') == 7:
            return self.validate_IPV6(queryIP)
        else:
            return 'Neither'

    def validate_IPV4(self, queryIP: str):
        nums = queryIP.split('.')
        for x in nums:

            if len(x) == 0 or len(x) > 3:
                return 'Neither'

            if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
                return 'Neither'

        return 'IPv4'

    def validate_IPV6(self, queryIP: str):
        nums = queryIP.split(':')
        hexdigits = '0123456789abcdefABCDEF'

        for x in nums:
            if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                return 'Neither'
        return 'IPv6'


so = Solution2()

# string = '172.16.254.1'

string = '12..33.4'

res = so.validIPAddress(string)


print(res)
