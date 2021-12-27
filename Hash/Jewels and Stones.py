
# Time O(J + S)

# Space O(J)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0

        j = set(jewels)

        for s in stones:
            if s in j:
                res += 1

        return res


so = Solution()


# jewels = "aA"
# stones = "aAAbbbb"

jewels = "z"
stones = "ZZ"

res = so.numJewelsInStones(jewels, stones)


print(res)
