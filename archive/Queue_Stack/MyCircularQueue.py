'''
own solution
'''


class MyCircularQueue:

    def __init__(self, k: int):
        self.items = [0] * k
        # for i in range(k):
        #     self.items.append(None)
        self.count = 0
        self.head = -1
        self.tail = -1  # available to insert
        self.capacity = k

    def enQueue(self, value: int) -> bool:

        if self.count == self.capacity:
            print('queque is full')
            return False

        if self.head == self.tail and self.count == 0:
            self.head += 1
            if(self.head == self.capacity):
                self.head = 0

        self.tail += 1

        if(self.tail == self.capacity):
            self.tail = 0

        self.items[self.tail] = value
        self.count += 1

        print(self.items, end="\t")
        print(f'head {self.head} tail {self.tail}')
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        # only one itme left
        if self.head == self.tail:
            self.count -= 1
            return True

        self.head += 1

        if(self.head == self.capacity):
            self.head = 0
        self.count -= 1

        print(f'size is {self.count}')
        print(self.head, self.tail)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.items[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.items[self.tail]

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.capacity == self.count:
            return True
        else:
            return False

        # Your MyCircularQueue object will be instantiated and called as such:
        # obj = MyCircularQueue(k)
        # param_1 = obj.enQueue(value)
        # param_2 = obj.deQueue()
        # param_3 = obj.Front()
        # param_4 = obj.Rear()
        # param_5 = obj.isEmpty()
        # param_6 = obj.isFull()


obj = MyCircularQueue(3)

param_1 = obj.enQueue(1)
param_1 = obj.enQueue(2)
param_1 = obj.enQueue(3)
param_1 = obj.enQueue(4)


# param_1 = obj.enQueue(8)
# print(obj.isEmpty())
