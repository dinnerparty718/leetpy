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

以层为概念的搜索方式，展开所有node,适合最短路径，图可能有玩，需要查重
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