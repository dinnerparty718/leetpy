import heapq


def findMedian(arr):
    # Write your code here
    max_heap_left = []

    # if odd, right heap has one more item
    min_heap_right = []

    res = []

    for num in arr:
        # 2   ,   3
        # 4

        # 4 2, 3
        # 2 , 3- > 4
        if len(max_heap_left) == len(min_heap_right):
            heapq.heappush(min_heap_right, -
                           heapq.heappushpop(max_heap_left, -num))
            res.append(min_heap_right[0])
        else:

            # 2 | 3 4
            # 2 | 3 4 5
            # 3 - 2 | 4, 5

            heapq.heappush(max_heap_left, -
                           heapq.heappushpop(min_heap_right, num))

            res.append((-max_heap_left[0] + min_heap_right[0]) // 2)

    return res


arr = [5, 15, 1, 3]

arr = [1, 2]

res = findMedian(arr)

print(res)
