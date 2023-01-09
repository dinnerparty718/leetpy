from typing import List


# can not use sort and two pointer
# don't need to reduce duplicate, just need to return the index
# use hashmap (a + b) = -(c + d)

# time O(n^2)
# space two hashap O(n^2) coudl be n^2 distinct a+b keys

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = 0
        m = {}
        for n1 in nums1:
            for n2 in nums2:
                # better approach to set default value
                m[n1+n2] = m.get(n1+n2, 0) + 1

        for n3 in nums3:
            for n4 in nums4:
                cnt += m.get(-(n3 + n4), 0)
        return cnt


nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]


so = Solution()

res = so.fourSumCount(nums1, nums2, nums3, nums4)


print(res)
