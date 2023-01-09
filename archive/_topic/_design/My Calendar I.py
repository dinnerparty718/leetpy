import bisect
from sortedcontainers import SortedList


# own yass! with sortedList

class MyCalendar:

    def __init__(self):
        # self.events = SortedList(key=lambda x: [x[0], x[1]])
        self.events = SortedList()

    def book(self, start: int, end: int) -> bool:
        interval = [start, end]

        if len(self.events) == 0:
            self.events.add(interval)
            return True

        insert_idx = self.events.bisect_right(interval)

        if interval == [8, 13]:
            print(insert_idx)

        if insert_idx == 0:
            if end <= self.events[insert_idx][0]:
                self.events.add(interval)
                return True
            else:
                return False
        elif insert_idx == len(self.events):
            if start >= self.events[len(self.events)-1][1]:
                self.events.add(interval)
                return True
            else:
                return False
        else:

            if start >= self.events[insert_idx-1][1] and end <= self.events[insert_idx][0]:
                self.events.add(interval)
                return True
            else:
                return False


#! https://leetcode.com/problems/my-calendar-i/discuss/1262532/Python-Sortedlist-solution-explained


# easy to insert

class MyCalendar:

    def __init__(self):
        #! trick
        self.events = SortedList([
            (float('-inf'), float('-inf')),
            (float('inf'), float('inf')),
        ])

    def book(self, start: int, end: int) -> bool:
        if end <= start:
            return False

        # case 1
        i = self.events.bisect_right((start,))

        if start >= self.events[i-1][1] and end <= self.events[i][0]:
            self.events.add((start, end))
            return True
        else:
            return False


# using bisect module
#! https://stackoverflow.com/questions/14895599/insert-an-element-at-a-specific-index-in-a-list-and-return-the-updated-list


class MyCalendar2:

    def __init__(self):
        # 1 D
        self.events = []

    def book(self, start: int, end: int) -> bool:
        if end <= start:
            return False

        i = bisect.bisect_right(self.events, start)

        # pairs
        if i % 2:
            return False

        j = bisect.bisect_left(self.events, end)

        if i != j:
            return False
        self.events[i:i] = [start, end]
        return True


cal = MyCalendar()

cal.book(47, 50)
cal.book(33, 41)
cal.book(25, 32)
cal.book(26, 35)
cal.book(19, 25)
cal.book(3, 8)
cal.book(8, 13)
# cal.book(0, 5)
# cal.book(5, 8)
# cal.book(8, 10)
# print(cal.book(8, 9))
# print(cal.book(0, 1))

for intervel in cal.events:
    print(intervel)

# [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
