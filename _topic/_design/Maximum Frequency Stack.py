from collections import defaultdict, Counter

'''
a,a,a,b,b, c
------------    
a: 1
max_freq = 1
group : [1] :[a]


a: 2
max_freq = 2
group : 
    1 :[a]
    2 :[a]
------------    
a: 3
max_freq = 3
group : 
    1 :[a]
    2 :[a]
    3 :[a]

a: 3, b: 1
max_freq = 3
------------    
group : 
    1 :[a,b]
    2 :[a]
    3 :[a]
------------    
a: 3, b: 1
max_freq = 3

group : 
    1 :[a,b]
    2 :[a]
    3 :[a]
------------   
a: 3, b: 2
max_freq = 3

group : 
    1 :[a,b]
    2 :[a,b]
    3 :[a]
------------   

a: 3, b: 2, c:1
max_freq = 3

group : 
    1 :[a,b,c]
    2 :[a,b]
    3 :[a]



------------   
pop()
x = group[max_freq].pop()

freq[x] -=1

if len(group[max_freq]) == 0:
    max_freq -=1


return x

'''


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
