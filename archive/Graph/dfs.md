## DFS

# using stack, return to previous state
# or recursion
# go as deep as possible

# time O(V + E)  vertices and edges
# space O(V)   stack or implicit reversion


## example problems

### find all paths from A to B

dfs(at):
    if visited[at]: return
    visted[at] = true

    neighbours = graph[at]
    for next in neighbours:
        dfs(next)

start_node = 0
dfs(start_node)


### finding connted components (count these components) eg number of island

global or class scope

n = number of nodes in the graph
g = adjacency list representing graph
count = 0
components = empy integer array # size n
visited = [false, false,..., false] # size n

findComponents():
    for i in range(n):
        if i not in visted:
            count+=1
            dfs(i)
    return (count, components)


dfs(at):
    visited[at] = true
    component[at] = count
    for next in graph[at]:
        if next not in visited:
            dfs(next)
