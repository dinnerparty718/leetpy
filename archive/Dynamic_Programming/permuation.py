from typing import List

'''

param(curr_idx, arr)

keep swap curr_idx and looping i
backtrack
when curr_idx == len(arr), copy arr to res
swap back

total permulation n! = n(n-1)(n-2)(n-3)*1 

n = 3 , permutations = 3*2*1 = 6

'''


class Solution:
    def permute_no_duplicate(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(curr_idx: int, curr: List[int]):

            if curr_idx == n:
                res.append(curr[:])
                return

            for i in range(curr_idx, n):
                curr[curr_idx], curr[i] = curr[i], curr[curr_idx]
                helper(curr_idx+1, curr)
                curr[curr_idx], curr[i] = curr[i], curr[curr_idx]

        helper(0, nums)

        return res


so = Solution()

nums = [1, 2, 3]
res = so.permute_no_duplicate(nums)

# print(res)


class Solution:
    def permute_with_dup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(index: int, nums: List[int]):
            if index == n:

                res.append(nums[:])
                return

            number_set = set()

            for i in range(index, n):
                nums[i], nums[index] = nums[index], nums[i]
                if nums[index] not in number_set:
                    helper(index+1, nums)
                    number_set.add(nums[index])
                nums[i], nums[index] = nums[index], nums[i]

        helper(0, nums)

        return res


so = Solution()

nums = [1, 2, 2]
res = so.permute_with_dup(nums)

print(res)
