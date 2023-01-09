from typing import List


# todo change memo data structure
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        memo = [None] * (len(s)+1)

        def dfs(s: str, n: int, wordDict: set, memo: List[bool]):
            if n == 0:
                return True

            if memo[n] != None:
                return memo[n]

            memo[n] = False

            for i in range(n):
                substr = s[i:n]

                if substr in wordDict:
                    left = dfs(s, i, wordDict, memo)
                    if left:
                        memo[n] = True

            return memo[n]

        res = dfs(s, len(s), wordDict, memo)

        print(memo)

        return res


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]


so = Solution()
res = so.wordBreak(s, wordDict)
print(res)
