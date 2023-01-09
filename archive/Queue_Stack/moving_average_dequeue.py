import collections
from typing import Deque

# time O(1)
# Space O(n) n is window size


class MovingAverage:

    def __init__(self, size: int):
        self.capacity = size
        self.queue: Deque[int] = collections.deque()

    def next(self, val: int) -> float:

        if len(self.queue) == self.capacity:
            self.queue.popleft()

        self.queue.append(val)

        return sum(self.queue) / len(self.queue)

        # Your MovingAverage object will be instantiated and called as such:
        # obj = MovingAverage(size)
        # param_1 = obj.next(val)


obj = MovingAverage(3)
param_1 = obj.next(1)
