import heapq


class MedianFinder:

    def __init__(self):
        self.max_heap = []  # left half
        self.min_heap = []  # right half, right half have one more item if len is odd

    def addNum(self, num: int) -> None:

        # add left, then add right
        if len(self.max_heap) == len(self.min_heap):

            heapq.heappush(self.min_heap, -
                           heapq.heappushpop(self.max_heap, - num))

        else:
            # add right, add left

            heapq.heappush(self.max_heap, -
                           heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0])/2
        else:
            return self.min_heap[0]
