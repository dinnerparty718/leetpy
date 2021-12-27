from typing import List
from collections import defaultdict

# build two sum hashmap, store the i,j array in the value

# 2 sum N^2
# total N^4


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        h_map = defaultdict(list)
        res_s = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                h_map[nums[i] + nums[j]].append([i, j])

        # for k, v in h_map.items():
        #     print(k, '\t', v)

        for key, value in h_map.items():
            comple = target - key

            if comple not in h_map:
                continue

            if comple == key:
                if len(value) == 1:
                    continue

            l1 = value

            l2 = h_map[comple]

            for item1 in l1:
                for item2 in l2:
                    if item2[0] > item1[1]:
                        res_s.add(
                            tuple(sorted([nums[item1[0]], nums[item1[1]], nums[item2[0]], nums[item2[1]]])))

        return [list(item) for item in res_s]


# nums = [1, 1]
# target = 2


nums = [-5, 5, 4, -3, 0, 0, 4, -2]
target = 4


so = Solution()

res = so.fourSum(nums, target)
print(res)
