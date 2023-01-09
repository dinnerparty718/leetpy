https://www.youtube.com/watch?v=vIXf2M37e0k&list=PLV5qT67glKSErHD66rKTfqerMYz9OaTOs&index=6



# heappushpop() vs heapreplace
## heappushpop()  more efficent then push then pop
## heapreplace pops first, then insert


# K largest

- sort O(nlogn)
- max heap 1.heapify 2 poll k times O(n+klogn)
- min heap keep k size min heap and poll  O(nlogk)   streaming one by one, size with 



## gereral steps, can be used as a stream

1. Initialize a min heap
2. for each element x in the array
   1. add to heap if heap size <k or x >= top of heap
   2. adjust heap size if necessary
3. Return the top of heap



# Merge K Sorted Lists

## merge 2 sorted lists -> two pointer

1. Linear Scan O(k)
2. Simple Sorting O(klogk)
3. Min Heap O(logk) can be used as a online algorithem


## Min heap O(nlogk) n = num of nodes 

### General Steps:

1. initialize min heap with all List head reference
2. while heap is not empty
   1. poll out top of heap (smallest pointer)
   2. add it to the result list
   3. add its next node if there exists


[[somebody](https://tyk-1.gitbook.io/py3-lc/gong-si-dian-mian-mian-jing/ixl_learning/h-23.-merge-k-sorted-lists)]