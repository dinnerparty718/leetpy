from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_map = {}

        stack = [nums2[0]]

        i = 1

        # while stack or i < len(nums2):
