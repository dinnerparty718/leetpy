'''
In this problem, you are given an integer N, and a permutation, P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N). You want to rearrange the elements of the permutation into increasing order, repeatedly making the following operation:
Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
Your goal is to compute the minimum number of such operations required to return the permutation to increasing order.
Signature
int minOperations(int[] arr)
Input
Array arr is a permutation of all integers from 1 to N, N is between 1 and 8
Output
An integer denoting the minimum number of operations required to arrange the permutation in increasing order
Example
If N = 3, and P = (3, 1, 2), we can do the following operations:
Select (1, 2) and reverse it: P = (3, 2, 1).
Select (3, 2, 1) and reverse it: P = (1, 2, 3).
output = 2

'''


import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

from collections import deque


def minOperations(arr):
    # Write your code here
    n = len(arr)

    target = [i for i in range(1, n+1)]

    visited = set([tuple(arr)])

    # print(visited)

    q = deque([arr])

    def neighbors(seq: list[int]):
        for i in range(n):
            for j in range(i+1, n):
                left = seq[:i]
                middle = seq[i:j+1]
                middle.reverse()
                right = seq[j+1:]
                # print(a + b)
                yield left + middle + right

    res = 0

    while q:

        size = len(q)

        for _ in range(size):
            seq = q.popleft()

            if seq == target:
                return res

            for nei in neighbors(seq):
                if tuple(nei) not in visited:
                    q.append(nei)
                    visited.add(tuple(nei))
        res += 1

    return -1

    # These are the tests we use to determine if the solution is correct.
    # You can add your own at the bottom.


def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number,
              ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    n_1 = 5
    arr_1 = [1, 2, 5, 4, 3]
    expected_1 = 1
    output_1 = minOperations(arr_1)
    check(expected_1, output_1)

    n_2 = 3
    arr_2 = [3, 1, 2]
    expected_2 = 2
    output_2 = minOperations(arr_2)
    check(expected_2, output_2)

# Add your own test cases here
