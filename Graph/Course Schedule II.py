from typing import List
from collections import defaultdict
from collections import deque
# topological order


# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# [0, 1] 0 depends on 1

# Time O(V + E)
# S O(v + E) queue + adjcency list
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        outdegree = defaultdict(set)
        indegree = [0] * numCourses

        # [u,v] means u is dependent on v

        for dest, src in prerequisites:
            outdegree[src].add(dest)
            indegree[dest] += 1

        q = deque()
        ans = []

        # there could me multiple course with indegree = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                ans.append(i)

        edge_count = len(prerequisites)

        while q:
            node = q.popleft()
            for x in outdegree[node]:
                edge_count -= 1
                indegree[x] -= 1
                if indegree[x] == 0:
                    q.append(x)
                    ans.append(x)

        if edge_count == 0:
            return ans
        else:
            return []


numCourses = 4


prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]


so = Solution()

res = so.findOrder(numCourses, prerequisites)

print(res)
