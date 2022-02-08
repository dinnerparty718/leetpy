from collections import defaultdict

# can be duplicates, as long as index are different


def numberOfWays(arr, k):
   # Write your code here
    h_map = defaultdict(int)

    res = 0

    for i, num in enumerate(arr):
        complement = k - num
        if complement in h_map:
            res += h_map[complement]
        h_map[num] += 1

    return res


arr = [1, 2, 3, 4, 3]
arr = [3, 3, 3, 3, 3]

res = numberOfWays(arr, 6)


print(res)
