# https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/196304/Verbosely-commented-Python-binary-search-approach-%2B-example-walkthrough
from typing import List

# todo need digest

# time sort O(nlog(n)) , binary search O(log(m)) (m is the max distance possible)  , count O(2n)-> O(n)   => O(nlog(m))
# space(1)


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        # cound how many distnace <= guess

        def possible(guess_dist):
            i = 0
            j = 1
            count = 0

            # two for loop?
            while i < len(nums):
                while j < len(nums) and (nums[j] - nums[i]) <= guess_dist:
                    j += 1

                count += j - i - 1
                i += 1

            return count >= k

        lo = 0
        # largtest possible distance
        hi = nums[-1] - nums[0]

        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid

            else:
                lo = mid + 1

        return lo


so = Solution()

nums = [1, 3, 1]
k = 1


res = so.smallestDistancePair(nums, k)


print(res)
