from typing import List


import heapq

# 1 heapify
# 2 pop item until len(q) = k
# 3 compare income value to top item. if < top item,drop the record
# if > top item poppush


# part 1 initialization
# heapify O(n) n is the len of the nums list
# remove until len(q) = k  O(nlogn)

# part2 add m times
# O (mlogk)


# space o(n)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = nums
        self.capacity = k
        heapq.heapify(self.q)

        while len(self.q) > k:
            heapq.heappop(self.q)

    def add(self, val: int) -> int:

        if len(self.q) < self.capacity:
            heapq.heappush(self.q, val)
            return self.q[0]

        top = self.q[0]
        if val <= top:
            return top
        else:
            heapq.heappushpop(self.q, val)
            return self.q[0]

        # Your KthLargest object will be instantiated and called as such:
        # obj = KthLargest(k, nums)
        # param_1 = obj.add(val)

# leet code version

# simpler but slower


class KthLargest2:

    def __init__(self, k: int, nums: List[int]):
        self.q = nums
        self.capacity = k
        heapq.heapify(self.q)
        while len(self.q) > k:
            heapq.heappop(self.q)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)

        if len(self.q) > self.capacity:
            heapq.heappop(self.q)

        return self.q[0]

# turing planet


class KthLargest3:

    def __init__(self, k: int, nums: List[int]):
        self.capacity = k
        self.data = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        # if not eaqual becomes distinct
        if len(self.data) < self.capacity or val >= self.data[0]:
            heapq.heappush(self.data, val)

        if len(self.data) > self.capacity:
            heapq.heappop(self.data)

        return self.data[0]


def main():
    k = 3
    nums = [4, 5, 8, 2]
    obj = KthLargest3(k, nums)

    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))
    print()

    nu = [1, 3, 4, 4, 4]

    heapq.heapify(nu)

    print(heapq.heappop(nu))
    print(heapq.heappop(nu))
    print(heapq.heappop(nu))
    print(heapq.heappop(nu))
    print(heapq.heappop(nu))


if __name__ == '__main__':
    main()
