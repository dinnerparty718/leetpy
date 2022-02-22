from typing import List


'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Approach 1 Brute Force O(n^2) half of the square
Approach 2 plot the price on chart

find largest peak following the smallest valley
min, max

Time O(n)
Space O(1)


'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit


so = Solution()

prices = [7, 1, 5, 3, 6, 4]
res = so.maxProfit(prices)


print(res)
