'''
There are n guests attending a dinner party, numbered from 1 to n. The ith guest has a height of arr[i-1] inches.
The guests will sit down at a circular table which has n seats, numbered from 1 to n in clockwise order around the table. As the host, you will choose how to arrange the guests, one per seat. Note that there are n! possible permutations of seat assignments.
Once the guests have sat down, the awkwardness between a pair of guests sitting in adjacent seats is defined as the absolute difference between their two heights. Note that, because the table is circular, seats 1 and n are considered to be adjacent to one another, and that there are therefore n pairs of adjacent guests.
The overall awkwardness of the seating arrangement is then defined as the maximum awkwardness of any pair of adjacent guests. Determine the minimum possible overall awkwardness of any seating arrangement.
Signature
int minOverallAwkwardness(int[] arr)
Input
n is in the range [3, 1000].
Each height arr[i] is in the range [1, 1000].
Output
Return the minimum achievable overall awkwardness of any seating arrangement.
Example
n = 4
arr = [5, 10, 6, 8]
output = 4
If the guests sit down in the permutation [3, 1, 4, 2] in clockwise order around the table (having heights [6, 5, 8, 10], in that order), then the four awkwardnesses between pairs of adjacent guests will be |6-5| = 1, |5-8| = 3, |8-10| = 2, and |10-6| = 4, yielding an overall awkwardness of 4. It's impossible to achieve a smaller overall awkwardness.



        1
    2  ___ 3 
   4  /   \  5
   6  \___/  7
      8   9


'''


from collections import deque
import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def minOverallAwkwardness(arr):
    # Write your code here
    arr.sort()
    print(arr)

    for a, b in zip(arr, arr[min(2, len(arr)-1):]):
        print(a, b)

    return max((abs(a-b) for a, b in zip(arr, arr[min(2, len(arr)-1):])))


def minOverallAwkwardness(arr):
    arr.sort()

    q = deque([])

    for i in range(len(arr)):
        if i % 2 == 0:
            q.append(arr[i])
        else:
            q.appendleft(arr[i])

    diff = abs(q[0] - q[-1])

    for i in range(1, len(arr)):
        diff = max(diff,  abs(q[i] - q[i-1]))

    return diff

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
    arr_1 = [5, 10, 6, 8]
    expected_1 = 4
    output_1 = minOverallAwkwardness(arr_1)
    check(expected_1, output_1)

    arr_2 = [1, 2, 5, 3, 7]
    expected_2 = 4
    output_2 = minOverallAwkwardness(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
