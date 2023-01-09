### Kahn's Algorithm for topological Sorting

Limitation

- Topological sorting” only works with graphs that are directed and acyclic.
- There must be at least one vertex in the “graph” with an “in-degree” of 0. If all vertices in the “graph” have a non-zero “in-degree”, then all vertices need at least one vertex as a predecessor. In this case, no vertex can serve as the starting vertex.

[https://leetcode.com/explore/learn/card/graph/623/kahns-algorithm-for-topological-sorting/3886/]
## In-Degree Out-Degree

Is there is a cycle, there is NO topological order

## Optimization
this step can be performed more efficiently by creating an adjacency list where adjacencyList[course] contains a list of courses that depend on course. Then when each course is taken, we will only iterate over the courses that have the current course as a prerequisite. 

Time  O(V + E) 
Space O(V + E)