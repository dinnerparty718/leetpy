import heapq
from queue import PriorityQueue
from collections import defaultdict
from Tree.TreeNode import TreeNode
a = PriorityQueue()


a = defaultdict(int)


a[0] = 1

print(a)

n1 = TreeNode(0)
n2 = TreeNode(0)
n3 = TreeNode(2)


ls = [(1, id(n1), n1), (1, id(n2), n2), (2, id(n3), n3)]

heapq.heapify(ls)


print(ls)
