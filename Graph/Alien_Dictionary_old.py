from typing import List
from collections import defaultdict
from collections import deque

# should not have any cycle


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        word_d = defaultdict(set)
        all_char = set()

        for word in words:
            for c in word:
                all_char.add(c)

        for k, v in word_d.items():
            print(k, v)

        # if len(words) == 1:
        #     return words[0][0]

        for index in range(1, len(words)):
            prev = words[index-1]
            cur = words[index]
            i, j = 0, 0

            while prev[i] == cur[j]:
                i += 1
                j += 1
                if i == len(prev) or j == len(cur):
                    break  # else won't execute

            else:
                word_d[prev[i]].add(cur[j])

        for k, v in word_d.items():
            print(k, v)

        if len(word_d) == 0:
            return ''

        # flat_list = [item for sublist in t for item in sublist]

        outList = []

        for values in word_d.values():
            outList.extend(values)

        entryPoint = None

        for key in word_d.keys():
            if key not in set(outList):
                entryPoint = key

        if not entryPoint:
            return ''

        res = []

        visited = set()

        def dfs(start: str, res: List[int], graph: dict):
            q = graph[start]
            while q:
                nei = q.pop()
                if nei not in visited:
                    dfs(nei, res, graph)

            res.append(start)
            visited.add(start)

        dfs(entryPoint, res, word_d)

        add = [c for c in all_char if c not in res]

        res = deque(res[::-1])

        print(res)

        for a in add:
            if a in word_d:
                res.appendleft(a)
            else:
                res.append(a)

        # res.extend(add)

        return ('').join(res)


so = Solution()
words = ["wrt", "wrf", "er", "ett", "rftt"]
# words = ["abc", "ab"]

res = so.alienOrder(words)

print(res)
