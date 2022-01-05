1. Dijkstra Algorithem
   - only for posiive edges
   - greedy

# todo
# https://www.youtube.com/watch?v=YMyO-yZMQ6g
Time O(V+ElogV)  Binary heap
Space O(V)

initailize table
V, weight, previous V
A
B
C
E

algo: (best first search)
1. set all nodes distances to float('inf') and start o 0
2. add (0, start, None) to pq
3. while pq is not empty
   - pop (d, cur, prev) from pq
   - if cur is not done, mark as done
   - for all edges 
     - if not yet done, put edegs in the queue (d+d2,nei, cur)


4. Bellman-Ford algorithm
   - Both positive and negative edges
   