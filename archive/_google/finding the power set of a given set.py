from typing import List


def findPowerSet(nums: List[int]):
    res = [[]]

    for n in nums:
        for i in range(len(res)):
            res.append([n] + res[i])

    return res


print(findPowerSet([0, 1, 2, 3]))
