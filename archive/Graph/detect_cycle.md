# detect cycle in directed graph

using 3 sets
    - white
    - gray
    - black
## using DFS

# Time O(E+V)
# Space O(V)
Move all the vertices from white to Black
if any one ended in grey. a cycle detected

link [https://www.youtube.com/watch?v=rKQaZuoUR4M]

[https://leetcode.com/problems/course-schedule-ii/]

# detect cycle in undirect graph
## disjoint set

Union two nodes one by one, until two nodes are already connected

## dfs need to keep track of the incoming node, using visited node set,