from typing import List


# https://leetcode.com/problems/interval-list-intersections/discuss/712920/Python-3-(classical-interval-intersection)
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        i, j = 0, 0

        res = []

        while i < len(firstList) and j < len(secondList):
            # a start first

            intersect_a_start = firstList[i][0] <= secondList[j][0] and secondList[j][0] <= firstList[i][1]

            # b start first
            intersect_b_start = secondList[j][0] <= firstList[i][0] and firstList[i][0] <= secondList[j][1]

            # over lap [max if start, min of end]
            if intersect_a_start or intersect_b_start:
                res.append([max(firstList[i][0], secondList[j][0]),
                            min(firstList[i][1], secondList[j][1])])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

            # b start first

            # move pointer

        return res


so = Solution()


firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]

# firstList = [[1, 3], [5, 9]]
# secondList = []

res = so.intervalIntersection(firstList, secondList)

print(res)
