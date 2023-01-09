# Mininum Spanning tree E = V -1

## two algo

Difference
“Kruskal’s algorithm” expands the “minimum spanning tree” by adding edges.
Whereas “Prim’s algorithm” expands the “minimum spanning tree” by adding vertices.




### Kruskal, to construct a mininum spanning tree of a "weighted undirected graph"
Time: time complexity is O(ElogE+Eα(V))=O(E⋅logE).
Space: O(V)
   1. sort edges
   2. selection minimul edges, skip the edge that forms a cycle
      1. to check if the edge form a cycle, can use disjoint set , check one edge O(α(V)), all edges O(E⋅α(V))
   3. until V-1 edges

### Prim "Prim's algorithm", that can be used to construct a “minimum spanning tree” of a “weighted undirected graph”.
Time: O(E⋅logV) for Binary heap
Space:  O(V)








