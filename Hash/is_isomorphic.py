# time O(n)
# space O(1) since character size is fixed

# own
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        if len(s) != len(t):
            return False

        for i, c in enumerate(s):
            if c in m and m[c] != t[i]:
                return False
            else:
                m[c] = t[i]

        return len(m.values()) == len(set(m.values()))


# todo can use zip function

class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1 = {}
        m2 = {}

        for c1, c2 in zip(s, t):
            if c1 not in m1 and c2 not in m2:
                m1[c1] = c2
                m2[c2] = c1
            elif m1.get(c1) != c2 or m2.get(c2) != c1:
                return False

        return True


class Solution3:
    def transformString(self, s: str) -> str:
        index_mapping = {}
        new_str = []

        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))

        return " ".join(new_str)

    def isIsomorphic(self, s: str, t: str) -> bool:
        # print(self.transformString(s))
        # print(self.transformString(t))
        return self.transformString(s) == self.transformString(t)


s = "egg"
t = "add"
# s

so = Solution3()

print(so.isIsomorphic(s, t))
