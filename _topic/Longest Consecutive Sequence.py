'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

using set
current + 1 and check in set

'''


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_steak = 0
        num_set = set(nums)

        for num in num_set:
            #! and we only attempt to build sequences from numbers that are not already part of a longer sequence.
            if num - 1 not in num_set:
                current_num = num
                current_steak = 1

                while current_num + 1 in num_set:
                    current_num += 1

                    current_steak += 1

                longest_steak = max(longest_steak, current_steak)

        return longest_steak


so = Solution()
nums = [100, 4, 200, 1, 3, 2]

# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

# nums = [1, 2, 0, 1]

res = so.longestConsecutive(nums)
print(res)
