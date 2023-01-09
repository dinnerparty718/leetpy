class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.count = 0
        self.items = [0]*size

        self.writeIdx = 0

    def next(self, val: int) -> float:
        if self.count != self.size:
            self.count += 1

        self.items[self.writeIdx % self.size] = val

        self.writeIdx += 1

        if self.count == self.size:
            return sum(self.items)/self.size
        else:
            return sum(self.items)/self.count

        # Your MovingAverage object will be instantiated and called as such:
        # obj = MovingAverage(size)
        # param_1 = obj.next(val)


obj = MovingAverage(4)

print(obj.next(1))
