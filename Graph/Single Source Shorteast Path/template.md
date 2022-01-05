### Dijkstra Algorithem
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


### Bellman-Ford algorithm
   - Both positive and negative edges
   - shortest path is at most N-1
   - acyclic graph + positive cycle, there is a shortest path
   - negative cycle there is no shortest path


at most N-1 iteration of 0,1,2,3,4   
order of the edges matter

SPFA algorithm (shortest path faster algorithm)
- stoping criteria queue is empty


### Comparison
- both use relaxing strategy
  - Dijkastra : greedy 
  - Bellman-Ford:  each node relax V-1 times at most



U -> V 

dU + W(U,V) < dV