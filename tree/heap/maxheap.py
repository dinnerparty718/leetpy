import heapq


class MaxHeap:
    def __init__(self, l=[]) -> None:
        if not l:
            self.storage = []
        else:
            self.storage = [-item for item in l]
            heapq.heapify(self.storage)

    def push(self, val: int):
        heapq.heappush(self.storage, -val)

    def peek(self):
        if len(self.storage):
            return self.storage[0] * -1
        else:
            return None

    def pop(self):
        if not self.size():
            return None
        return heapq.heappop(self.storage)

    def size(self):
        return len(self.storage)


def main():
    l = [3, 4, 5, 2, 7]

    maxHeap = MaxHeap(l)

    maxHeap.push(9)

    print(maxHeap.storage)
    maxHeap.pop()
    print(maxHeap.peek())
    print(maxHeap.storage)


if __name__ == '__main__':
    main()
