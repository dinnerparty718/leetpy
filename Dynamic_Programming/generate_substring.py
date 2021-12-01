
from typing import List


s = 'abcde'

# generate all substring (n * (n + 1)) / 2


def substring(s: str) -> List[List[str]]:
    n = len(s)

    res = []

    for s_len in range(1, n+1):
        for idx in range(n):
            if idx + s_len <= n:
                res.append(s[idx:idx + s_len])

    return res


res = substring(s)

print(len(res))
