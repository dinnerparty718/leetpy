from typing import Counter, List
from collections import defaultdict


#! never alter the container you're looping on
#! error message dictionary changed size during iteratiion
#! Option 1 iterate through copy
#! Option 2 list/dict/set comprehension
# time O(V + E)
# space O(V)
class Solution:
    def has_cycle(self, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        white = set()
        grey = set()
        black = set()

        for s, t in edges:
            graph[s].append(t)
            white.add(s)
            white.add(t)

        def move_vertext(current: int, src_set: set, dest_set: set):
            src_set.remove(current)
            dest_set.add(current)

        def dfs(current: int):
            move_vertext(current, white, grey)

            for nei in graph[current]:
                if nei in black:
                    continue
                if nei in grey:
                    return True
                if dfs(nei) == True:
                    return True
            move_vertext(current, grey, black)
            return False  # not cycle deteced

        #! avoid python for loop while modifying the app
        while len(white) > 0:
            # each time iter(white) is a new object
            current = next(iter(white))
            if dfs(current) == True:
                return True

        return False


edges = [[1, 2], [1, 3], [2, 3], [4, 1], [4, 5], [5, 6], [6, 4]]


so = Solution()
res = so.has_cycle(edges)

print(res)
