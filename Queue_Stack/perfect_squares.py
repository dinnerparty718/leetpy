

# n-ary tree find shortest path using BFS

class Solution:
    def numSquares(self, n: int) -> int:
        # find all number's sqaure < n
        square_nums = [i*i for i in range(1, int(n ** 0.5) + 1)]

        level = 0

        queue = {n}

        while queue:
            #! Important: use set() instead of list() to eliminate the redundancy,
            next_queue = set()
            level += 1

            for remainder in queue:
                for square_num in square_nums:
                    if remainder == square_num:
                        return level
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder-square_num)
            queue = next_queue
        return level


solution = Solution()


res = solution.numSquares(13)

print(res)
