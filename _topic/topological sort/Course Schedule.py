from typing import List
from collections import defaultdict, deque
# build in and out ajacent list
# can finish all courses
# [ 0, 1 ]  1 -> 0


# https://leetcode.com/problems/course-schedule/solution/
# todo try DFS or backtracking

# add node when in_degree == 0 to queue


# Time O(E + V) E is the number of dependencies (edge) V is number of courses
# dictionary + in_degree count
# Space O(E + V)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        out_degree = defaultdict(list)
        in_degree = [0] * numCourses

        for nextCourse, preCourse in prerequisites:
            out_degree[preCourse].append(nextCourse)
            in_degree[nextCourse] += 1

        queue = deque()
        res = []  # ! either keep an order or count edges

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            res.append(course)

            for next_couse in out_degree[course]:
                in_degree[next_couse] -= 1
                if in_degree[next_couse] == 0:
                    queue.append(next_couse)

        # build list

        return numCourses == len(res)


so = Solution()


numCourses = 2

prerequisites = [[1, 0], [0, 1]]

res = so.canFinish(numCourses, prerequisites)


print(res)
