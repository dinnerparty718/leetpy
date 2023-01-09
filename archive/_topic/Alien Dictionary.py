from typing import List
from collections import defaultdict
from collections import deque


# using Kahn's Algorithm for Topological sorting

# https://leetcode.com/problems/alien-dictionary/discuss/492056/Python-Fast-Topological-sort-solution-with-detailed-explanation

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        res = []
        if not words:
            return ''
        outdegree = defaultdict(set)

        all_c = set()

        for i in range(len(words)):
            for c in words[i]:
                all_c.add(c)

        # words = 'z'
        # ! special case
        if len(all_c) == 1:
            return all_c.pop()

        indegree = {}

        for c in all_c:
            indegree[c] = 0

        for i in range(1, len(words)):
            prev = words[i-1]
            curr = words[i]

            p1 = p2 = 0

            while p1 < len(prev) and p2 < len(curr) and prev[p1] == curr[p2]:

                p1 += 1
                p2 += 1

                if p1 == len(prev) or p2 == len(curr):
                    # ! special case
                    # ['abc', 'ab'] special case
                    if len(prev) > len(curr):
                        return ''

            if p1 < len(prev) and p2 < len(curr):
                outdegree[prev[p1]].add(curr[p2])

        for v in outdegree.values():
            for c in v:
                indegree[c] += 1

        q = deque()

        for k, v in indegree.items():
            if v == 0:
                q.append(k)
                # del indegree[k]
                #! don't delete the key whil iterate the dict

        while q:
            c = q.popleft()
            res.append(c)
            del indegree[c]

            for w in outdegree[c]:
                indegree[w] -= 1
                if indegree[w] == 0:
                    q.append(w)

        return ''.join(res) if len(res) == len(all_c) else ''


so = Solution()

#words = ["wrt", "wrf", "er", "ett", "rftt"]

words = ["qb", "qts", "qs", "qa", "s"]
#words = ['abc', 'ab']

# "jkrtw"

res = so.alienOrder(words)


print(res)
