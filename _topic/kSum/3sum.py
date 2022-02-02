from typing import List


# leetcode
# outer loop + two sum


# Time O(n^2) twoSum O(n) sort O(nlogn)
# space O(n) or O(logn) depends on the sorting implementation

# Sort + (two pointers) or (Hashset)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break  # can't find and solution for sure
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSumII(nums, i, res)

        return res

    # two pointer
    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i+1, len(nums)-1
        while lo < hi:
            three_sum = nums[i] + nums[lo] + nums[hi]
            if three_sum < 0:
                lo += 1
            elif three_sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])

                # ! continue to search for more answers
                lo - +1
                hi -= 1

                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i+1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j+1]:
                    j += 1
            seen.add(nums[j])
            j += 1


# non-sort
# when you can't modify the input array
# since you can't sort, use a hashset to store sorted (a,b,c) to avoid duplicate
# Time O(n^2)
# space O(n) for the hashmap
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = {}  # compliment and it's current i

        dups = set()
        res = set()

        for i in range(len(nums)):
            if nums[i] not in dups:
                dups.add(nums[i])
                for j in range(i+1, len(nums)):
                    complement = -nums[i] - nums[j]
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((nums[i], nums[j], complement))))
                    seen[nums[j]] = i

        return res


nums = [-1, 0, 1, 2, -1, -4]


so = Solution()

res = so.threeSum(nums)

print(res)
