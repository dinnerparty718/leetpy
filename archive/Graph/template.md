# Graph
- 可能有环
- 分为无向和有向图
- 没有固定入口
- 可能有多个入口


## Graph Representatioin

- adjacency matrix   if graph is big and very few edeges, memory waste
- adjacency list    good for memory if ew edeges



### Adjacenty List
最常用两个实现方式( list可用set 代替)

- List<T>[n]
  - 
- Map<T, List<T>>
  - adjList.get(i): All neighbors of node i




## BFS (Breadth-First Search)

以层为概念的搜索方式,展开所有node,适合最短路径,图可能有玩,需要查重
找最短路径只适用物uniform cost （每条edge的weight一样）



### BFS模板

1. Initialize a Queue for **all starting points** , a HashSet to record visited node
2. while queue is not empty
   1. Retrieve current queue size as number of nodes in the current level
   2. for each node in current level
      1. poll out on node
      2. if this is the node we want, return it
      3. offer all its neghbors to the queue **if not visited and valid**
   3. increase level


2d matrix matrix[i][j] -> 4 directions

[[0,1],[0,-1],[1,0],[-1,0]]


## BFS2 (Best-First Search)

针对Non-uniform cost graph的一种算法 核心思想是优先展开最“优”节点 **use heap**

Dijsktra's Algorithm

### BFS2模板 基本与BSF相同 queue 换 heap (priority queue)
1. Initialize a Heap for **all starting points** , a HashSet to record visited node
2. while heap is not empty
   1. Poll out one node
   2. skip it if visited
   3. otherwise mark node as visited, update its cost
   4. if this is the destination node, return
   5. for all of it's neighbors, offer them in to the heap with current node's cost + edge cost

Time: O((E + V)logV)
Space: O(V)
每个Node可以被添加进heap多次,但只能被展开一次

#### build graph (or dict) using adjacent list
d[src] = [dest,cost]



## DFS (Depth-First Search)

### DFS模板
1. Initialize Hashset to record visited nodes
2. for all entry nodes, call dfs()
   1. validate current node , if visited or invalid or anwer node, return  **(2.1 and 3.1 choose one)
   2. Do Something (Pre-order)
   3. For each neighbor node
      1. validate neighbor node, if visited or invalid or answer node, don't recursion on it or return answer
      2. recurse down on neightbor node ->dfs(neighbor)
   4. Do something (post-order)

