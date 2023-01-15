'''
8 · Rotate Character Array

time O(n)
space O(1) -> in place

[1,2,3,4,5,6,7]  k = 3    => [5,6,7,1,2,3,4] 


# revser whole array
7,6,5,4,3,2,1

# reverse first [0, k -1]
5,6,7

# reverse k

1,2,3,4


'''

from typing import (
    List,
)


class Solution:
    """
    @param s: An array of char
    @param offset: An integer
    @return: nothing
    """

    def rotate_string(self, s: List[str], offset: int):
        # write your code here
        k = offset % len(s)

        def reverse(start: int, end: int):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        reverse(0, len(s)-1)
        reverse(0, k-1)
        reverse(k, len(s)-1)


so = Solution()


s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


res = so.rotate_string(s, 3)
print(s)


'''
189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass
