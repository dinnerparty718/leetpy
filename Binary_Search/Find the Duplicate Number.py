from typing import List

'''
287. Find the Duplicate Number


高斯
1 + 2 + 3 + 4 =  (1 + 4) * 4 /2 = 10
Sum(nums) = 10 = 2


'''

# todo  binary search method

# cycle detection
# hare and tortois


# time O(n)
# space O(1)
# does not modify element

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            # cycle found
            if fast == slow:
                break

        # find intersection (entrance)
        # slow start from entry point
        # fast start from where they meet

        slow = nums[0]

        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]

        return fast

# Array as Hashmap

# Time O(n)
# space O(1)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            # nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
            # ! order matter
            nums[0], nums[nums[0]] = nums[nums[0]], nums[0]

        return nums[0]


# Array as Hashmap (recurisve)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def store(nums: List[int], cur: int) -> int:
            if cur == nums[cur]:
                return cur
            nxt = nums[cur]
            #! chnage array here
            nums[cur] = cur
            return store(nums, nxt)
        return store(nums, 0)


# flip to -negative
# ! remember to restore the nums
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for num in nums:
            val = abs(num)
            if nums[val] < 0:
                duplicate = val
                break
            nums[val] = - nums[val]

        # restore numbers

        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate


so = Solution()

nums = [1, 3, 4, 2, 2]
nums = [3, 1, 3, 4, 2]


res = so.findDuplicate(nums)


print(res)
