from collections import defaultdict, Counter


class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.max_freq = 0
        self.group = defaultdict(list)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > self.max_freq:
            self.max_freq = self.freq[val]

        self.group[self.freq[val]].append(val)

    def pop(self) -> int:
        x = self.group[self.max_freq].pop()

        self.freq[x] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return x
