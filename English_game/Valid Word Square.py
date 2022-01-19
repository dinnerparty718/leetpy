from typing import List


# own slow

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        lengh = [len(words)] + [len(word) for word in words]

        n = max(lengh)

        grid = [[''] * n for _ in range(n)]

        for i, word in enumerate(words):
            for j, c in enumerate(word):
                grid[i][j] = c

        for i in range(n):
            for j in range(n):

                if i == j:
                    continue
                if grid[i][j] != grid[j][i]:
                    return False

        return True


words = ["abcd", "bnrt", "crmy", "dtye"]

words = ["abcd", "bnrt", "crm", "dt"]

words = ["ball", "area", "read", "lady"]


so = Solution()


res = so.validWordSquare(words)


print(res)
