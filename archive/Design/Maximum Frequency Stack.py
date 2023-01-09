from collections import defaultdict, Counter


class FreqStack:

    def __init__(self):
        self.freq = Counter()  # for the count
        self.group = defaultdict(list)  # stack with frequency
        self.maxfreq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.maxfreq:
            self.maxfreq = f

        self.group[f].append(val)

    def pop(self) -> int:
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1

        # check group size
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x


FS = FreqStack()

FS.push(5)
FS.push(7)
FS.push(5)
FS.push(7)
FS.push(4)
FS.push(5)

FS.pop()
FS.pop()
FS.pop()
FS.pop()


print(FS.freq)
print(FS.group)
print('max freq', FS.maxfreq)
