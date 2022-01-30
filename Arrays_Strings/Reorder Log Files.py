
from typing import List


# own, custom sort
# success at first try!
# ! practice python custom sort

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        value_logs = []

        def processLog(log: str):
            i = 0
            key = []
            while i < len(log) and log[i] != ' ':
                key.append(log[i])
                i += 1

            # i stop at first empty string

            is_digit_log = True

            for j in range(i+1, len(log)):
                if log[j].isalpha():
                    is_digit_log = False

            return (is_digit_log, ''.join(key), log[i+1:])

        for idx, log in enumerate(logs):
            is_digit_log, key, value = processLog(log)
            # print(is_digit_log, key, value)
            if is_digit_log:
                digit_logs.append(logs[idx])
            else:
                value_logs.append((key, value, idx))

        sorted_value_logs = sorted(value_logs, key=lambda x: [x[1], x[0]])

        return [logs[log[2]] for log in sorted_value_logs] + digit_logs


so = Solution()

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]

logs = ["a1 9 2 3 1", "g1 act car",
        "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
res = so.reorderLogFiles(logs)

print(res)
