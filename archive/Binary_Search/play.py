from collections import defaultdict
import bisect

l = [1, 2, 3, 4, 5, 6]

# return a insertion point
i = bisect.bisect_left(l, 0)

print(i)

# insert the value
bisect.insort_left(l, 0)
print(l)


graph = defaultdict(list)


a = graph['b']

print(a)
