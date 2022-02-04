from typing import List


# two kind of log
# 1. digit - dig1 8 1 5 1
# 2. letter - let3 art zero

class Log:
    def __init__(self, logStr: str) -> None:
        first_space = logStr.index(' ')

        self.key = logStr[0:first_space]
        self.value = logStr[first_space+1:]
        self.logStr = logStr
        # digit type 1,
        # letter char 0
        self.type = 1 if all(
            ch in '0123456789 ' for ch in self.value) else 0

    def __lt__(self, other) -> bool:

        if self.type < other.type:
            return True
        else:
            if self.type == 0:
                if self.value < other.value:
                    return True

                if self.value == other.value:
                    return self.key < other.key


#! python use Timesort

# N - Number of logs
# M - max length of a single log

# Time O(M * NlogN)  M * compare the key
# Space M * N to kee the keys for the log

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        #! only split once

        def get_key(log: str):
            _id, rest = log.split(' ', maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else(1, None, None)

        return sorted(logs, key=get_key)


# use lambda key function


so = Solution()

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]

res = so.reorderLogFiles(logs)


print(res)
