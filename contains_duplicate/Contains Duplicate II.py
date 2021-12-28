from typing import List


# hashmap
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h_map = {}

        for end in range(len(nums)):
            num = nums[end]

            if num in h_map:
                if end - h_map[num] <= k:
                    return True

            h_map[num] = end

        return False


# maintain a k window of set
#! there is no indices concept in python set, convert it to list will cost O(n) time

# set
# more memory efficent seen is only store k value
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i-k])  # ! evict the least-recently seen

        return False


so = Solution()
nums = [1, 2, 3, 1]
k = 3

nums = [1, 2, 3, 1, 2, 3]
k = 2
res = so.containsNearbyDuplicate(nums, k)

print(res)
