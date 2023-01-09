'''
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

 
'''


from typing import List


# sliding windowse
# valid ->  count of zero <2
#  invalid  -> count of zero >=2
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0

        cnt_of_zeros = 0
        res = 0

        while right < n:
            if nums[right] == 0:
                cnt_of_zeros += 1

            while cnt_of_zeros == 2:
                if nums[left] == 0:
                    cnt_of_zeros -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1
        return res


so = Solution()

nums = [1, 0, 1, 1, 0]

res = so.findMaxConsecutiveOnes(nums)


print(res)
