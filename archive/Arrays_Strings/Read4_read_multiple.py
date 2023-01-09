# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

from typing import List
from collections import deque

'''
store remaning in queue

'''


class Solution:

    def __init__(self) -> None:
        self.q = deque([])

    def read(self, buf: List[str], n: int) -> int:
        total_read = 0

        def read4(buf4):
            pass

        while self.q and n > 0:
            buf[total_read] = self.q.popleft()
            total_read += 1
            n -= 1

        while n > 0:
            buf4 = ['']*4
            current_read = read4(buf4)
            if current_read == 0:
                return total_read

            # read > need
            if current_read > n:
                self.q.extend(buf4[n:current_read])

            for i in range(min(current_read, n)):
                buf[total_read] = buf4[i]
                total_read += 1
                n -= 1
        return total_read
