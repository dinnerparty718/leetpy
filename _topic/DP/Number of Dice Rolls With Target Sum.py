'''
You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target.
Since the answer may be too large, return it modulo 109 + 7.

n : num of dice
k:  num of face

#! all possible values for one dice 1 - k

seen on rocket reach hacker rank questions
p = numRollsToTarget / all_possible outcome ( k ** n)



# todo bottom up


'''


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (n + 1) for _ in range(1, target+2)]

        for row in dp:
            print(row)


class Solution1:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        memo = {}

        MOD = 10**9 + 7

        def helper(target: int, num_of_dice: int):
            if target <= 0 or target > num_of_dice * k:
                return 0
            if num_of_dice == 1:
                return 1

            if (target, num_of_dice) in memo:
                return memo[(target, num_of_dice)]

            res = 0

            # try all possible values
            for i in range(1, k + 1):
                res += helper(target - i, num_of_dice - 1)

            memo[(target, num_of_dice)] = res

            return memo[(target, num_of_dice)]

        return helper(target, n) % MOD


so = Solution()


n = 2
k = 6
target = 7


# n = 30
# k = 30
# target = 500

res = so.numRollsToTarget(n, k, target)


print(res)
