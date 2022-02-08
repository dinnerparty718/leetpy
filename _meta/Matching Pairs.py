'''
Matching Pairs
Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s and t after swapping exactly two characters within s.
A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively. The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.
Note: This means you must swap two characters at different indices.
Signature
int matchingPairs(String s, String t)
Input
s and t are strings of length N
N is between 2 and 1,000,000
Output
Return an integer denoting the maximum number of matching pairs
Example 1
s = "abcd"
t = "adcb"
output = 4
Explanation:
Using 0-based indexing, and with i = 1 and j = 3, s[1] and s[3] can be swapped, making it  "adcb".
Therefore, the number of matching pairs of s and t will be 4.
Example 2
s = "mno"
t = "mno"
output = 1
Explanation:
Two indices have to be swapped, regardless of which two it is, only one letter will remain the same. If i = 0 and j=1, s[0] and s[1] are swapped, making s = "nmo", which shares only "o" with t.

'''

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


# abcde
# adcbe

def matching_pairs(s, t):
    # Write your code here

    # These are the tests we use to determine if the solution is correct.
    # You can add your own at the bottom.
    n = len(s)

    unMatchedPair = set()

    matched = set()
    count = 0

    isDup = False

    for i in range(n):
        if s[i] == t[i]:
            count += 1
            if s[i] in matched:
                isDup = True
            matched.add(s[i])
        else:
            unMatchedPair.add((s[i], t[i]))

    if count == n:
        return count if isDup else count - 2

    # aba aby
    #
    # aab aac
    # abb aba

    if count == n - 1:
        a, b = unMatchedPair.pop()

        # aba abb
        # aab aac
        if isDup or a in matched or b in matched:
            return count

        return count - 1

    for a, b in unMatchedPair:
        if (b, a) in unMatchedPair:
            return count + 2

    unMatchS = set()
    unMatchT = set()

    # partial match
    for a, b in unMatchedPair:
        if a in unMatchT or b in unMatchS:
            return count + 1
        unMatchS.add(a)
        unMatchS.add(b)

    return count


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
    s_1, t_1 = "abcde", "adcbe"
    expected_1 = 5
    output_1 = matching_pairs(s_1, t_1)
    check(expected_1, output_1)

    s_2, t_2 = "abcd", "abcd"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    # Add your own test cases here

    s_2, t_2 = "aa", "aa"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    s_2, t_2 = "ax", "ay"
    expected_2 = 0
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    s_2, t_2 = "axb", "ayb"
    expected_2 = 1
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    s_2, t_2 = "axa", "aya"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    s_2, t_2 = "abx", "abb"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    s_2, t_2 = "abb", "axb"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    s_2, t_2 = "ax", "ya"
    expected_2 = 1
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)
