from typing import List
from collections import defaultdict

# own solution
# can remove sort to make itlinear


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        res = {}
        for i, c in enumerate(list1):
            d[c] = i

        for i, c in enumerate(list2):
            if c in d:
                res[c] = d[c] + i
        m_val = min([val for val in res.values()])

        return [key for key, value in res.items() if value == m_val]

# optimzied


class Solution2:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        res = {}
        for i, c in enumerate(list1):
            d[c] = i

        for i, c in enumerate(list2):
            if c in d:
                if not res:
                    res[c] = d[c] + i
                else:
                    if d[c] + i < list(res.values())[0]:
                        res = {c: d[c] + i}
                    elif d[c] + i == list(res.values())[0]:
                        res[c] = d[c] + i

        return list(res.keys())


# further optimized store [] and min seperately instead of a dict
class Solution3:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        res = []
        min_cnt = float('inf')
        for i, c in enumerate(list1):
            d[c] = i

        for i, c in enumerate(list2):
            if c in d:
                if not res:
                    res.append(c)
                    min_cnt = d[c] + i
                else:
                    if d[c] + i < min_cnt:
                        res.clear()
                        res.append(c)
                    elif d[c] + i == min_cnt:
                        res.append(c)

        return res


so = Solution3()


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]


print(so.findRestaurant(list1, list2))
