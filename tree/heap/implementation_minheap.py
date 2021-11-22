class MinHeap:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0
        self.storage = [0] * capacity

    def insert(self, data):
        if self.isFull():
            return
        self.storage[self.size] = data
        self.size += 1
        # self.heapifyUp_iterative()
        self.heapifyUp(self.size - 1)

    def delete(self) -> int:
        if self.size == 0:
            return
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1

        self.heapifyDown(0)

        return data

    def heapifyDown_interative(self):
        index = 0

        while self.has_left_child(index):
            smaller_index = self.left_idx(index)
            if self.has_right_child(index) and self.left_child(index) > self.right_child(index):
                smaller_index = self.right_idx(index)

            if self.storage[index] > self.storage[smaller_index]:
                self.swap(index, smaller_index)
            index = smaller_index

    def heapifyDown(self, index):
        if not self.has_left_child(index):
            return

        smaller_index = self.left_idx(index)
        if self.has_right_child(index) and self.left_child(index) > self.right_child(index):
            smaller_index = self.right_idx(index)

        if self.storage[index] > self.storage[smaller_index]:
            self.swap(index, smaller_index)

        self.heapifyDown(smaller_index)

    def heapifyUp_iterative(self):
        index = self.size - 1

        while self.has_parent(index) and self.storage[index] < self.parent(index):
            self.swap(index, self.parent_idx(index))
            index = self.parent_idx(index)

    def heapifyUp(self, index):
        if self.has_parent(index) and self.parent(index) > self.storage[index]:
            self.swap(index, self.parent_idx(index))
            self.heapifyUp(self.parent_idx(index))

    def parent(self, index):
        return self.storage[self.parent_idx(index)]

    def left_child(self, index):
        return self.storage[self.left_idx(index)]

    def right_child(self, index):
        return self.storage[self.right_idx(index)]

    def parent_idx(self, index):
        return (index - 1) // 2

    def left_idx(self, index):
        return 2 * index + 1

    def right_idx(self, index):
        return 2 * index + 2

    def has_parent(self, index):
        return self.parent_idx(index) >= 0

    def has_left_child(self, index):
        return self.left_idx(index) < self.size

    def has_right_child(self, index):
        return self.right_idx(index) < self.size

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]
        # temp = self.storage[index1]
        # self.storage[index1] = self.storage[index2]
        # self.storage[index2] = temp


def main():
    heap = MinHeap(7)

    heap.insert(2)
    heap.insert(4)
    heap.insert(7)
    heap.insert(10)
    heap.insert(8)
    heap.insert(9)

    minVal = heap.delete()

    print(minVal)

    print(heap.size)

    print(heap.storage)


if __name__ == '__main__':
    main()
