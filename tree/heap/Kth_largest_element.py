from typing import List


import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = heapq.heapify(nums)
        return

    def add(self, val: int) -> int:
        pass
        # Your KthLargest object will be instantiated and called as such:
        # obj = KthLargest(k, nums)
        # param_1 = obj.add(val)


def main():
    l = [2, 3, 1, 7, 5, 4]
    heapq.heapify(l)


if __name__ == '__main__':
    main()
