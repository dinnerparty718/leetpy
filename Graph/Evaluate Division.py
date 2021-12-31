from typing import List
from collections import defaultdict


# union find variatoin  no array, no index
# todo

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        grid_weight = {}

        def find(node_id):
            if node_id not in grid_weight:
                # add to it's same group
                grid_weight[node_id] = (node_id, 1)  # group_id, weight
            group_id, node_weight = grid_weight[node_id]

            if group_id != node_id:
                pass
                # step 1 build the union groups

        def union(dividend, divisor, value):
            pass

        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)


so = Solution()


equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
values = [1.5, 2.5, 5.0]
queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]

res = so.calcEquation(equations, values, queries)
print(res)
