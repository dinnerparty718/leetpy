# min heap
# Time complexity: adding/inserting: O(log(n)), heapify the heap (build the heap): O(n)


import heapq


li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

heapq.heapify(li1)

print("The 3 largest numbers in list are : ", end="")
print(heapq.nlargest(3, li1))


print("The 3 smallest numbers in list are : ", end="")
print(heapq.nsmallest(3, li1))


# initializing list
li = [5, 7, 9, 1, 3]


# using heapify to convert list into heap  (O(n))
hi = heapq.heapify(li)


print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
