# solution1
# solution2  optimized two push stack pop stack

# time Amortized O(1) worst case O(n)
# space o(n)

class MyQueue:

    def __init__(self):
        # stack
        self.s1 = []
        self.s2 = []
        self.front = None  # keep track of the first item of s1

    def push(self, x: int) -> None:

        if len(self.s1) == 0:
            self.front = x

        self.s1.append(x)

    def pop(self) -> int:
        # pop check pop queue, if size is 0, move all times from push stack to pop stack

        if len(self.s1) + len(self.s2) == 0:
            return

        if len(self.s2) == 0:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        else:
            return self.front

    # is empty
    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0
        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()


obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())

print(obj.pop())
print(obj.empty())
