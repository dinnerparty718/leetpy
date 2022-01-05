from typing import List


# k + 1 iteration
# using two arrays to keep swapping
# n start from 0

# todo
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], s: int, dst: int, k: int) -> int:
        distances = [[float('inf')] * n for _ in range(2)]

        distances[0][s] = distances[1][s] = 0

        # i&1, 1-i&1
        # can also use odd,even

        # iter 0
        # current array = 0&1 = 0
        # previous array = 1 - (0&1) = 1

        # iter 1
        # current array = 1&1 = 1
        # previous array = 1 - (1&1) = 0

        # 0 - k (k+1) in total
        for iterations in range(k+1):
            # if iterations == 1:
            #     break
            for s, d, wUV in flights:
                # prvious
                dU = distances[1 - iterations & 1][s]

                # current
                dV = distances[iterations & 1][d]

                if dU + wUV < dV:
                    distances[iterations & 1][d] = dU + wUV

        return -1 if distances[k & 1][dst] == float('inf') else distances[k & 1][dst]


# https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/686939/Python-by-DP-with-Bellman-Ford-algorithm-w-Comment
# much easy to understand
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], s: int, dst: int, k: int) -> int:
        price_table = [float('inf')] * n

        # print(price_table)
        price_table[s] = 0

        # print(price_table)

        # initialization with 0 transfer

        for source, destination, ticket_price in flights:
            if source == s:
                price_table[destination] = ticket_price

        # tranfer k times to update price table

        for transfer in range(k):
            current_price = [*price_table]  # use price_table[:]

            #! important use previous source, if source was updated this round, des will be updated in enxt round
            for source, destination, ticket_price in flights:
                current_price[destination] = min(
                    price_table[source] + ticket_price, current_price[destination])

            price_table = current_price

        return -1 if price_table[dst] == float('inf') else price_table[dst]


n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 1


so = Solution()

res = so.findCheapestPrice(n, flights, src, dst, k)


print(res)
