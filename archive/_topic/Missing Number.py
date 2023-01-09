from typing import List


'''
#! 0 ^ n = n
#! 5 ^ 3 ^ 5 = 5 ^ 5 ^ 3


XOR
O(N) O(1)


2 ^ 3
10
11
01  -> 1

5 ^ 5
101
101
000


[3, 0, 1] ^ [ 0,1,2,3 ]
= 3^0^1^0^1^2^3
= 3^3 ^ 0^0 ^ 1^1 ^ 2
= 0 ^ 0 ^ 0 ^2
= 2

 
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)

        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

# Time O(n)
# space O(1)
# math formular


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        actual_sum = sum(nums)

        # formular

        #  1 + ...  n
        #  (n+1)n/2
        # expeted_sum = sum([i for i in range(1, n+1)])
        expeted_sum = (n+1) * n // 2

        return expeted_sum - actual_sum

# Time O(nlogn)
# space O(1) or O(n)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return len(nums)


so = Solution()

nums = [3, 0, 1]
res = so.missingNumber(nums)

print(res)
