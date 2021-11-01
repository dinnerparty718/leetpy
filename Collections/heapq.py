import heapq

li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

heapq.heapify(li1)

print("The 3 largest numbers in list are : ", end="")
print(heapq.nlargest(3, li1))


print("The 3 smallest numbers in list are : ", end="")
print(heapq.nsmallest(3, li1))
