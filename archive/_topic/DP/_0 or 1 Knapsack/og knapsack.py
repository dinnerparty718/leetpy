# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RM1BDv71V60

#! top down with memo
# time Time O(n*c) n is length of array, c is capacity
# space O(n*c)
def solve_knapsack(profits, weights, capacity):

    memo = {}
    n = len(profits)
    # pick or not pick

    # two states -> 2D
    def helper(i: int, capacity: int):
        if i == n or capacity < weights[i]:
            return 0

        if (i, capacity) in memo:
            return memo[(i, capacity)]

        profit1 = helper(i+1, capacity - weights[i]) + profits[i]
        profit2 = helper(i+1, capacity)

        memo[(i, capacity)] = max(profit1, profit2)
        return memo[(i, capacity)]

    return helper(0, capacity)

#! top down with memo 2d


def solve_knapsack(profits, weights, capacity):
    n = len(profits)

    #! i,capacity
    dp = [[-1] * (capacity + 1) for _ in range(n)]

    def knapsack(i: int, capacity: int):
        if i == n or capacity < weights[i]:
            return 0
        if dp[i][capacity] != -1:
            return dp[i][capacity]

        profit1 = knapsack(i+1, capacity - weights[i]) + profits[i]
        profit2 = knapsack(i+1, capacity)

        dp[i][capacity] = max(profit1, profit2)
        return dp[i][capacity]

    return knapsack(0, capacity)


#! bottom up DP

def solve_knapsack(profits, weights, capacity):
    n = len(profits)

    # edge cases
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    #! also initailize for all i's when capacity == 0
    dp = [[0] * (capacity + 1) for _ in range(n)]

    for capacity in range(1, capacity + 1):
        if weights[0] <= capacity:
            dp[0][capacity] = profits[0]

    for i in range(1, n):
        for capacity in range(1, capacity + 1):

            #! can be optimized here, we only need row i-1 for current row i

            # exclude the item
            profit1 = dp[i-1][capacity]

            # include the item, if it is not more than the capacity
            profit2 = dp[i-1][capacity - weights[i]] + profits[i] if weights[i] <= capacity else 0

            dp[i][capacity] = max(profit1, profit2)

    print_selected_elements(dp, weights, profits, capacity)

    return dp[n-1][capacity]

# todo


def print_selected_elements(dp: list[list[int]], weights: list[int], profits: list[int], capacity: int):
    print("Selected weights are: ", end='')
    n = len(weights)
    totalProfit = dp[n-1][capacity]

    for i in range(n-1, 0, -1):
        if totalProfit != dp[i-1][capacity]:
            # i must be included
            print(str(weights[i]) + " ", end='')
            capacity -= weights[i]
            totalProfit -= profits[i]
    if totalProfit != 0:
        print(str(weights[0]) + " ", end='')
    print()


def main():
    # print(solve_knapsack([4, 5, 3, 7], [2, 3, 1, 4], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    # print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
