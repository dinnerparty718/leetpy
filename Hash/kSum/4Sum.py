from typing import List
from collections import defaultdict

# todo make recursive function for ksum


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # def findNsum(nums, target, N, result, results):
        #     # early termination
        #     if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
        #         return
        #     if N == 2:  # two pointers solve sorted 2-sum problem
        #         l, r = 0, len(nums)-1
        #         while l < r:
        #             s = nums[l] + nums[r]
        #             if s == target:
        #                 results.append(result + [nums[l], nums[r]])
        #                 l += 1
        #                 while l < r and nums[l] == nums[l-1]:
        #                     l += 1
        #             elif s < target:
        #                 l += 1
        #             else:
        #                 r -= 1
        #     else:  # recursively reduce N
        #         for i in range(len(nums)-N+1):
        #             if i == 0 or (i > 0 and nums[i-1] != nums[i]):
        #                 findNsum(nums[i+1:], target-nums[i],
        #                          N-1, result+[nums[i]], results)

        # results = []
        # findNsum(sorted(nums), target, 4, [], results)
        # return results

        nums.sort()
        # res = set()

        res = []

        for i in range(len(nums)):
            # skip duplicate in outer loop
            if i == 0 or nums[i] != nums[i-1]:

                for j in range(i+1, len(nums)):

                    if j == i+1 or nums[j] != nums[j-1]:

                        subset = self.twoSum2(
                            nums[j+1:], target - nums[i] - nums[j])

                        l = [nums[i], nums[j]]

                        for pair in subset:

                            # res.add(tuple(l + pair))
                            res.append((l + pair))

        return res

    def twoSum2(self, nums: List[int],  target: int):
        l, r = 0, len(nums)-1

        res = []

        while l < r:
            two_sum = nums[l] + nums[r]

            if two_sum > target:
                r -= 1
            elif two_sum < target:
                l += 1
            else:
                res.append([nums[l], nums[r]])
                l += 1

                while l < r and nums[l] == nums[l-1]:
                    l += 1

        return res


nums = [-1, 0, -5, -2, -2, -4, 0, 1, -2]

target = -9


so = Solution()

res = so.fourSum(nums, target)
print(res)
