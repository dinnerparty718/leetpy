from typing import List
from collections import deque, defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # special cases
        if not numCourses:
            return []

        if not prerequisites:
            return [i for i in range(numCourses)]

        outdegree = defaultdict(set)
        indegree = [0] * numCourses
        q = deque()
        res = []

        for dest, src in prerequisites:
            outdegree[src].add(dest)
            indegree[dest] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            course = q.popleft()
            res.append(course)

            for c in outdegree[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

        return res if len(res) == numCourses else []


so = Solution()


numCourses = 4

# dest src
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]


res = so.findOrder(numCourses, prerequisites)


print(res)
