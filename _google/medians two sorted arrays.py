
from typing import List

'''

median

odd
n // 2


even

(n//2 -1  +  n//2) 

#! same size n

1. Brute Force: merging using extra space
2. Two-pointers : couting while merging
3. divide and conquer -> binary search




#! different size m, n

'''


#! binary search recursive
def getMedian(A: List[int], B: List[int], n: int):

    #! base case
    if n == 0:
        return 0

    if n == 1:
        return (A[0] + B[0]) / 2

    middle1 = getArrayMedian(A, n)
    middle2 = getArrayMedian(B, n)

    if middle1 == middle2:
        return middle1

    if middle1 < middle2:
        return getMedian(A + )

    def getArrayMedian(C: List[int], n):
        if n % 2 == 0:
            return (C[n//2 - 1] + C[n//2])/2
        else:
            return C[n//2]


#! two pointer
#! 2n even length
#! n-1 n index
# Time O(n)
# space O(1)
def getMedian(A: List[int], B: List[int], n: int):
    i = 0
    j = 0

    middle1 = 0
    middle2 = 0
    count = 0

    while count <= n:

        if A[i] <= B[j]:
            middle1 = middle2  # store the previous median
            middle2 = A[i]
            i += 1
        else:
            middle1 = middle2
            middle2 = B[j]
            j += 1

        # edge case
        # 1 2 3
        # 5 6 7
        if i == n:
            middle1 = middle2
            middle2 = B[0]
            break
        elif j == n:
            middle1 = middle2
            middle2 = A[0]
            break

        count += 1

    return (middle1 + middle2)/2


arr1 = [1, 2, 3]
arr2 = [4, 5, 6]


print(getMedian(arr1, arr2, 3))


def getMedianFromSortedArray(nums: List[int]) -> float:
    n = len(nums)

    if n % 2 == 0:
        return (nums[n//2 - 1] + nums[n//2]) / 2
    else:
        return nums[n // 2]


nums = [1, 2, 3, 4, 5]
