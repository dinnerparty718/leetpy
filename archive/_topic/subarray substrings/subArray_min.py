# [3], [1], [2], [4], [3, 1], [1, 2], [2, 4], [3, 1, 2], [1, 2, 4], [3, 1, 2, 4]
# number of subarray n (n+1) / 2 = 4 * 5 / 2 = 10

# one pass, left boundary , right boundary

# left[i], the length of strictly larger numbers on the left of A[i],
# right[i], the length of larger numbers on the right of A[i].
'''
one pass, left boundary , right boundary
stack = []

next_smaller [n] * n
prev_smaller  [-1] * n 



'''


# 907. Sum of Subarray Minimums


def sumSubarrayMins(arr: list[int]):
    MOD = 10**9 + 7
    n = len(arr)
    next_smaller = [n] * n

    #! previous smaller or equal
    prev_smaller = [-1] * n

    stack = []

    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] > num:
            idx = stack.pop()
            next_smaller[idx] = i
        stack.append(i)

    stack = []

    # 约定, 5,5,5, 可以向左边扩展
    for i in reversed(range(n)):
        num = arr[i]
        while stack and arr[stack[-1]] >= num:
            idx = stack.pop()
            prev_smaller[idx] = i
        stack.append(i)

    # print(prev_smaller)

    res = 0

    for i in range(n):
        left = i - prev_smaller[i]
        right = next_smaller[i] - i
        res += (arr[i] * left * right) % MOD

    return res % MOD


arr = [3, 1, 2, 4]


res = sumSubarrayMins(arr)

print(res)

#! genrate the subarray

# for i in range(n):
#     for j in range(i, n):
#         print(arr[i:j+1], '\t\t', i, j)
