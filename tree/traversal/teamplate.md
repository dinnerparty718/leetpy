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

