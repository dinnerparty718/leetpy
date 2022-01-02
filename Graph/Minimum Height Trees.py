from typing import List
from collections import defaultdict


# for tree like, no more than two centroids   (for even nodes, 2, for odd number tree, 1)

# Time O(|V|) V number of nodes in the graph
# Space O(|V|)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # spacial case
        if n <= 2:
            return [i for i in range(n)]

        outdegree = defaultdict(set)

        for s, t in edges:
            outdegree[s].add(t)
            outdegree[t].add(s)

        leaves = []

        for key in outdegree:
            if len(outdegree[key]) == 1:
                leaves.append(key)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n

        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []

            while leaves:
                leaf = leaves.pop()

                # remove nodes from the graph, from both link
                # if only neibor left for the left node
                neighbor = outdegree[leaf].pop()
                outdegree[neighbor].remove(leaf)

                if len(outdegree[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # next round
            leaves = new_leaves

        return leaves


n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]

so = Solution()

res = so.findMinHeightTrees(n, edges)

print(res)
