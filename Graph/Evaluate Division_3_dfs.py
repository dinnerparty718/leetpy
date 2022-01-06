from typing import List
from collections import defaultdict

# own DFS
# Yass. don't modify the query


# N input equation, M number of queries
# Time O(M*N)
# Space O(N) graph

class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (divident, divisor), value in zip(equations, values):
            graph[divident].append((divisor, value))
            graph[divisor].append((divident, 1/value))

        # for k, v in graph.items():
        #     print(k, v)

        res = []

        def dfs(node: str, target: str, val: float, visited: set):
            if node == target:
                return True, val

            visited.add(node)

            for nei, v in graph[node]:
                if nei not in visited:
                    found, result = dfs(nei, target, val * v, visited)

                    if found:
                        return True, result

            return False, -1

        for divident, divisor in queries:
            if divident not in graph or divisor not in graph:
                # case 1 eaither nodes does not eixst
                res.append(-1.0)
            elif divident == divisor:
                res.append(1.0)

            else:
                found, result = dfs(divident, divisor, 1.0, set())
                res.append(result)

        return res


equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
values = [1.5, 2.5, 5.0]
queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]


so = Solution()

res = so.calcEquation(equations, values, queries)


print(res)
