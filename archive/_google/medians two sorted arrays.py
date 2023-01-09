'''

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

#! log hints binary search
#! binary search on the smaller array 

without merging them


always round down   total_len // 2

Total 13

6 + 7


B 1 2 3, 4 5 6 7 8 

A 1 2 3, 4 5 
  L        R
  

when even
    min(leftA, leftB) , max(rightA, rightB)  
when odd
    max(rightA, rightB)
    
    
log(min(n,m))    
'''


from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A)-1

        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B index

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if (i + 1) < len(A) else float('inf')

            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if (j + 1) < len(B) else float('inf')

            # partition is corrent
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                else:
                    # even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
