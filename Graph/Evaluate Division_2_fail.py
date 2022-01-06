from typing import List


# own DFS
# can't handle "aa" "a"

class Solution:

    def minimize(self, pair: List[str]):

        a = pair[0]
        b = pair[1]
        if len(a) == len(b) == 1:
            return pair

        a_set = {c for c in a}
        b_set = {c for c in b}

        common = a_set & b_set

        return [''.join(a_set - common), ''.join(b_set - common)]

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        res = []

        for e, quotient in zip(equations, values):

            equation = self.minimize(e)

            divident = equation[0]
            divider = equation[1]

            if divident in graph:
                graph[divident].append((divider, quotient))
            else:
                graph[divident] = [(divider, quotient)]

            if divider in graph:
                graph[divider].append((divident, 1 / quotient))
            else:
                graph[divider] = [(divident, 1 / quotient)]

        # for k, v in graph.items():
        #     print(k, v)

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

        for query in queries:
            a, b = self.minimize(query)
            if a not in graph or b not in graph:
                res.append(-1.0)
            elif a == b:
                res.append(1.0)
            else:
                found, result = dfs(a, b, 1.0, set())
                res.append(result)

        return res


equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
values = [1.5, 2.5, 5.0]
queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]


a = "bc"
b = "cd"


so = Solution()

res = so.calcEquation(equations, values, queries)


print(res)
