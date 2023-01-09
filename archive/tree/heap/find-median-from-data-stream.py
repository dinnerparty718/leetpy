import heapq


# own
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.size = 0

    def addNum(self, num: int) -> None:

        # max_heap has more
        if len(self.min_heap) == len(self.max_heap):
            val = heapq.heappushpop(self.max_heap, -num)
            val2 = heapq.heappushpop(self.min_heap, -val)
            heapq.heappush(self.max_heap, -val2)
        else:
            val = heapq.heappushpop(self.max_heap, -num)
            heapq.heappush(self.min_heap, -val)

        self.size += 1

    def findMedian(self) -> float:
        if self.size % 2 == 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0])/2


# better logn
class MedianFinder2:

    def __init__(self):
        self.max_heap = []  # smaller half
        self.min_heap = []  # larger half has one more

    def addNum(self, num: int) -> None:
        # min_heap has more item
        if len(self.min_heap) == len(self.max_heap):
            # add left then right
            heapq.heappush(self.min_heap, -
                           heapq.heappushpop(self.max_heap, -num))
        else:
            # add right to left

            heapq.heappush(self.max_heap, -
                           heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0])/2
        else:
            return self.min_heap[0]


obj = MedianFinder()
obj.addNum(2)
obj.addNum(3)
obj.addNum(4)

print(obj.max_heap)
print(obj.min_heap)

param_2 = obj.findMedian()
print(param_2)
