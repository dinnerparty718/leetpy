from collections import defaultdict, deque
from re import U
from typing import List


'''
Graph

construct graph
email -> email
#! vertice  email
#! edge


for all email in candidate

run BFS and return list of connected email group, group.sort()

and remove email from candidate set






N  number of account
K max length of an accounts 

worse case all email belone to one person

total number of emails = NK
BFS/DFS travle NK

sort NlogN

Time O(NKlogNK)
Space O(NK)


'''


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        graph = {}
        emailName = {}  # email - to  - email

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email] = []
                emailName[email] = name

        for account in accounts:
            for first, second in zip(account[1:], account[2:]):
                graph[first].append(second)
                graph[second].append(first)

        #! all vertics
        candidates = set(graph.keys())

        res = []

        def bfs(email: str):
            visited = set([email])
            q = deque([email])

            group = []
            while q:
                size = len(q)

                for _ in range(size):
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

                    for i in g:
                        candidates.remove(i)

        return res


class UF:

    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[x] > self.rank[y]:
            self.root[y] = root_x
        elif self.rank[x] < self.rank[y]:
            self.root[x] = root_y
        else:
            self.root[y] = root_x
            self.rank[root_x] += 1

    def find(self, x):

        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])

        return self.root[x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


'''
Union fin
'''


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))

        oweership = {}

        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in oweership:
                    uf.union(i, oweership[email])
                oweership[email] = i

        # append email to correct index

        ans = defaultdict(list)
        for email, owner in oweership.items():
            ans[uf.find(owner)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]


so = Solution()


accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"]
]

res = so.accountsMerge(accounts)


print(res)
