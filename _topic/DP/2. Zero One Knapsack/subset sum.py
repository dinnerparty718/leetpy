from doctest import REPORTING_FLAGS


def subset_sum(nums: list[int], target: int):
    n = len(nums)
    dp = [[None] * (target + 1) for _ in range(n)]

    # initialation when target = 0
    #! populate first column

    for i in range(n):
        dp[i][0] = True

    #! populate first row

    for j in range(1, target+1):
        dp[0][j] = nums[0] == j

    for i in range(1, n):
        for j in range(1, target+1):

            curr = nums[i]
            target_sum = j

            if target_sum < curr:
                dp[i][j] = dp[i-1][j]
            elif target_sum == curr:
                dp[i][j] = True
            else:
                if dp[i-1][j] == True:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i-1][target_sum - curr]

    # for row in dp:
    #     print(row)

    return dp[-1][-1]


nums = [1, 2, 3, 7]
target = 6


def main():
    print(subset_sum(nums, target))
    print(subset_sum([1, 2, 7, 1, 5], 10))
    print(subset_sum([1, 3, 4, 8], 6))


if __name__ == '__main__':
    main()
