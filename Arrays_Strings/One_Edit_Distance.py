from collections import defaultdict

'''

#todo 
one pass

short, long

loop through shorter one

can skip
delep




'''


class Solution2:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)

        # ensure s is shorter than t
        # better than swap
        if ns > nt:
            return self.isOneEditDistance(t, s)

        # more than one length diff
        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt:
                    #! replace one
                    return s[i+1:] == t[i+1:]
                else:
                    #! skip longer one
                    return s[i:] == t[i+1:]

        # 'ab'
        # 'a'

        return ns + 1 == nt


# own solution


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        diff = 0

        same_size = len(s) == len(t)

        if same_size:
            while p1 < len(s):
                if s[p1] != t[p2]:
                    diff += 1

                p1 += 1
                p2 += 1
            return diff == 1
        else:

            if len(s) > len(t):
                s, t = t, s

            if len(t) - len(s) > 1:
                return False

            while p1 < len(s):

                if s[p1] != t[p2]:
                    break
                p1 += 1
                p2 += 1
            return t[p2+1:] == s[p1:]


so = Solution2()

s = "acbbcda"
t = " abbdad"


res = so.isOneEditDistance(s, t)

print(res)
