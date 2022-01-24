from typing import List


# Own merge

# todo use two pointer
# https://leetcode.com/problems/interval-list-intersections/discuss/712920/Python-3-(classical-interval-intersection)
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # firstList.sort(key=lambda x: x[0])
        # secondList.sort(key=lambda x: x[0])

        event = []
        res = []

        for f in firstList:
            start, end = f
            event.append((start, 0))
            event.append((end, 1))

        for s in secondList:
            start, end = s
            event.append((start, 0))
            event.append((end, 1))

        event.sort(key=lambda x: [x[0], x[1]])

        # for e in event:
        #     print(e)

        cur = []
        count = 0

        for val, type in event:
            if type == 0:
                count += 1
            else:
                count -= 1

            if count == 2 and not cur:
                cur.append(val)
            elif count == 1 and len(cur) == 1:
                cur.append(val)
                res.append(cur[:])
                cur = []

        return res


so = Solution()


firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]

firstList = [[1, 3], [5, 9]]
secondList = []

res = so.intervalIntersection(firstList, secondList)

print(res)
