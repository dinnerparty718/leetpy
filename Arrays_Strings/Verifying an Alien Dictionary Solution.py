from typing import List
from collections import defaultdict


# label as easy

# todo check leetcode

# https://leetcode.com/problems/verifying-an-alien-dictionary/solution/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        graph = defaultdict(list)

        w_set = set()

        w1 = words[0]
        for w2 in words[1:]:
            p1 = 0
            p2 = 0
            n1 = len(w1)
            n2 = len(w2)

            while p1 < n1 and p2 < n2 and w1[p1] == w2[p2]:
                p1 += 1
                p2 += 1

            if p2 >= n2 and n1 > n2:
                return False

            if p1 < n1 and p2 < n2:
                graph[w1[p1]].append(w2[p2])
                w_set.add(w1[p1])
                w_set.add(w2[p2])

            w1 = w2

        # iterate thought graph

        # for k, v in graph.items():
        #     print(k, v)

        # print(w_set)

        l = []

        for c in order:
            if c in w_set:
                l.append(c)

        for k, v in graph.items():

            idx1 = l.index(k)

            for val in v:

                idx2 = l.index(val)
                if idx1 > idx2:
                    return False

        return True


so = Solution()

words = ["hello", "leetcode"]


# in this case, return false
# words = ["apple", "app"]


order = "hlabcdefgijkmnopqrstuvwxyz"


words = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"

# words = ["hello", "hello"]
# order = "abcdefghijklmnopqrstuvwxyz"


words = ["zirqhpfscx", "zrmvtxgelh", "vokopzrtc", "nugfyso", "rzdmvyf",
         "vhvqzkfqis", "dvbkppw", "ttfwryy", "dodpbbkp", "akycwwcdog"]
order = "khjzlicrmunogwbpqdetasyfvx"

res = so.isAlienSorted(words, order)

print(res)
