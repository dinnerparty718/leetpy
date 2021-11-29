from typing import List


# bottom up
# need to get answer for sub problem

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [None] * (n+1)  # (0->n)
        wordSet = set(wordDict)

        def dfs(l, memo, s, wordSet) -> bool:
            # base case
            if l == 0:
                return True
            # check memo
            if memo[l] != None:
                return memo[l]

            memo[l] = False

            for i in range(l):
                r = s[i:l] in wordSet
                if not r:
                    continue

                left = dfs(i, memo, s, wordSet)

                if left:
                    memo[l] = True
                    break

            return memo[l]

        # inital state biggest problem [0,n)

        return dfs(n, memo, s, wordSet)


so = Solution()


s = "leetcode"
wordDict = ["leet", "code"]

res = so.wordBreak(s, wordDict)

print(res)
