
# Graph Traverse 

## Time O(V + E)
    go through every Vertices and every Edges
## Space O(V) Stack or Recursion stack for all the Vertices

V - Vertices
E - Edges



# Traversing all paths between two vertices

## Complete Graph
A complete graph is a graph where every vertex is connected to every other vertex

In a complete graph, there will be V-1 unique paths of length one that start at the source vertex;
Next choice V-2

## Time O((V-1)!)  排列组合
## Space O(V^3)
