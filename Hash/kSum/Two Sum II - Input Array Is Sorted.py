from typing import List

# two pointer

# Time O(n)
# Space O(1)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            cur_sum = numbers[l] + numbers[r]

            if cur_sum < target:
                l += 1
            elif cur_sum > target:
                r -= 1
            else:
                return [l, r]


numbers = [2, 7, 11, 15]
target = 9

so = Solution()
res = so.twoSum(numbers, target)

print(res)
