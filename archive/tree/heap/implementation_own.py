from typing import List


# left child 2i + 1
# right child 2i + 2
# parent  floor ((i-1)/2)

# heapify need to start from the internal node
# own

class MinHeap:
    def __init__(self, data: List[int] = []) -> None:
        self.data = data
        if self.data:
            self.heapify()

    def heapify_down(self, i: int):
        while self.l_child(i):
            minChild_idx = self.l_idx(i)

            if self.r_child(i):
                if self.r_child(i) < self.data[minChild_idx]:
                    minChild_idx = self.r_idx(i)

            if self.data[i] > self.data[minChild_idx]:
                self.swap(i, minChild_idx)
                i = minChild_idx
            else:
                break

    def heapify_up(self, i: int):

        while self.parent(i) is not None and self.data[i] < self.parent(i):
            p_idx = self.p_idx(i)
            self.swap(p_idx, i)
            i = p_idx

    def insert(self, val: int):
        self.data.append(val)

        self.heapify_up(len(self.data)-1)

    # pop the first item, move last item to the top and heapify down

    def pop(self):
        if not self.data:
            return None

        val = self.data[0]
        self.data[0] = self.data.pop()

        self.heapify_down(0)

        return val

    # append at the end, heapify up

    def heapify(self):
        n = len(self.data)

        #! start from the internal node backwards
        for i in reversed(range(n)):
            self.heapify_down(i)

    def swap(self, index1: int, index2: int):
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]

    def l_idx(self, i):
        return 2*i + 1

    def r_idx(self, i):
        return 2*i + 2

    def l_child(self, i):
        l_index = self.l_idx(i)
        if l_index < len(self.data):
            return self.data[l_index]
        else:
            return None

    def r_child(self, i):
        r_index = self.r_idx(i)
        if r_index < len(self.data):
            return self.data[r_index]

    def p_idx(self, i):
        return (i - 1) // 2

    def parent(self, i):
        p_index = self.p_idx(i)
        if p_index >= 0:
            return self.data[p_index]
        else:
            return None


#nums = [8, 7, 9]
nums = [9, 7, 6, 4, 2, 3]
min_heap = MinHeap(nums)

print(min_heap.data)


min_heap.pop()

print(min_heap.data)


min_heap.insert(1)

print(min_heap.data)
