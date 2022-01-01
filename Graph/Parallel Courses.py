from typing import List
from collections import defaultdict, deque


# own Yass!
# topological sort
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        outdegree = defaultdict(set)
        indegree = [0] * (n+1)
        indegree[0] = -1  # no course 0
        q = deque()

        for pre, next in relations:
            outdegree[pre].add(next)
            indegree[next] += 1

        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)

        # print(q)

        seq = []
        cnt = 0
        while q:
            size = len(q)
            cnt += 1

            for i in range(size):
                course = q.popleft()
                seq.append(course)
                for c in outdegree[course]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        q.append(c)

        return cnt if len(seq) == n else -1


so = Solution()

n = 3
relations = [[1, 2], [2, 3], [3, 1]]


res = so.minimumSemesters(n, relations)

print(res)
