Time O(n), best case scenario, worse O(n) item is increasing

1. define buckets for arrays nums lowerBound upperBound
   1. buckets = [] * n
   2. insert nums[i] into bucket[n*nums[i]]
2. for each bucket, use other sorting algorithem, typically insertion sort (fast insert with linkedList)
