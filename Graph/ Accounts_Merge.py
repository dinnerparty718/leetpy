from typing import List
from collections import defaultdict
from collections import deque


# https://leetcode.com/problems/accounts-merge/discuss/721527/Easy-to-read-solutions-in-3-methods%3A-Union-Find-Graph-%2B-DFS-Graph-%2B-BFS
# todo disjoint set
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # undirected graph
        graph = {}

        emailName = {}

        # populate all email

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email] = []
                emailName[email] = name

        candidates = set(graph.keys())

        for account in accounts:
            for first, second in zip(account[1:], account[2:]):
                graph[first].append(second)
                graph[second].append(first)

        res = []

        def bfs(email: str):
            visited = set([email])

            q = deque([email])

            group = []

            while q:

                size = len(q)
                for _i in range(size):
                    e = q.popleft()
                    group.append(e)

                    for nei in graph[e]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)

            group.sort()

            return group

        for email in graph.keys():
            if email in candidates:
                g = bfs(email)

                if g:
                    name = emailName[g[0]]
                    res.append([name] + g)

                    # elimiate email
                    for i in g:
                        candidates.remove(i)
        return res


# leecode discussion
class Solution2:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        em_to_name = {}
        em_graph = defaultdict(set)

        for acc in accounts:
            name = acc[0]

            # only connect email 1 to rest email to form a star
            email1 = acc[1]
            em_to_name[email1] = name

            for email2 in acc[2:]:
                em_graph[email1].add(email2)
                em_graph[email2].add(email1)

                # create a hashmap
                # it help us to find the email owners
                em_to_name[email2] = name

        seen = set()
        ans = []

        for email in em_to_name:
            if email not in seen:
                s = [email]
                seen.add(email)
                emails = []

                while s:
                    cur = s.pop()
                    emails.append(cur)

                    for nei in em_graph[cur]:
                        if nei not in seen:
                            s.append(nei)
                            seen.add(nei)

                ans.append([em_to_name[email]] + sorted(emails))

        return ans


so = Solution2()

accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"]
]


# result = [
#     ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
#     ["Mary", "mary@mail.com"],
#     ["John", "johnnybravo@mail.com"]]


res = so.accountsMerge(accounts)

print(res)
