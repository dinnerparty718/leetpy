from typing import List
from collections import defaultdict


# union find variatoin  no array, no index
# todo

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        pass


so = Solution()


equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
values = [1.5, 2.5, 5.0]
queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]

res = so.calcEquation(equations, values, queries)
print(res)
