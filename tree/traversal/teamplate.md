# BFS (Breadth-First Search)

按“层”在概念进行的搜索， 用queue记录需要被展开的treenote


## BFS General Steps

1. Initialize Queue with all entry points
2. While queue is not empty
   1. for each node in the queue (currently) size = len(q)
   2. poll out the element (add to result)
   3. expand it, offer children to the queue in order
   4. increase level

each node in queue onnce O(n)


# DFS (Depth-First Search)
垂直概念，每个node visit三次

## DFS
1. Base Case
2. Either
   - DoSomething()
   - Recurse for subproblems



## Top Down vs. Bottom UP

### Top Down DFS
- 把值通过参数的形式从上往下传
- 一般dfs()本身不返回值

General Steps
1. Base Case
2. 利用父问题传下来的值做一些计算
3. 若有必要，做一些额外操作
4. 把值传下去给子问题继续递归 


### Bottom Up DFS （更难也更常见）
- 把值从下(subproblem)往上传
- 当前递归层利用subproblem传上来的值计算当前层的新值并返回
- 一定会有返回值

General Steps
1. Base Case
2. 向子问题要条案 (return value)
3. 利用子问题的答案构建当前问题（当前递归层)的答案
4. 若有必要，做一些额外操作
5. 返回答案(给父问题)