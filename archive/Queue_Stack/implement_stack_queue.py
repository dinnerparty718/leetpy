from collections import deque

# adjust while pushhing


class MyStack:

    def __init__(self):
        self.push_q = []
        self.pop_q = []

    def push(self, x: int) -> None:
        self.push_q.append(x)
        while self.pop_q:
            self.push_q.append(self.pop_q.pop(0))

        self.push_q, self.pop_q = self.pop_q, self.push_q

    def pop(self) -> int:
        return self.pop_q.pop(0)

    def top(self) -> int:
        return self.pop_q[0]

    def empty(self) -> bool:
        return len(self.push_q) + len(self.pop_q) == 0

        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()


# adjust while poping

class MyStack2:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        tmp = self.q1.pop(0)

        self.q1, self.q2 = self.q2, self.q1

        return tmp

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        tmp = self.q1.pop(0)

        self.q2.append(tmp)

        self.q1, self.q2 = self.q2, self.q1

        return tmp

    def empty(self) -> bool:
        return len(self.q1) + len(self.q2) == 0

        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()


# using only one queue

class MyStack2:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

        for i in range(len(self.queue)):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()
