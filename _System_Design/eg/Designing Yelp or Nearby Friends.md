
how to store location (static, places location dont change much)

https://www.educative.io/module/lesson/grokking-system-design-interview/B8KVZm1mwJW


1 SQL
2 Grids
    sparsed. dense
    unevenly distributed
    memory
3 dynamic size grids. quad tree -> much better way
    >500 break down to 4 square
    start from root. recursive search until a grid does not have children

    How much memory will be needed to store the QuadTree
    12.01 GB

    further we can do data partition in case the places growther also to serve more read traffic
    a. sharding based on regions -> hot spot, some regions are densed
    b.  sharding based on location id
        QuadTree structure on different partitions?