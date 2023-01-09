from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)

        for i in range(n):
            for j in range(len(words[i])):
                #! to check index error
                try:
                    if words[i][j] != words[j][i]:
                        return False
                except:
                    return False
        return True


so = Solution()

words = ["abcd", "bnrt", "crmy", "dtye"]
# words = ["ball", "area", "read", "lady"]

# words = ["abcd", "bnrt", "crm", "dt"]

words = ["ball", "asee", "let", "lep"]
words = ["abcd", "bnrt", "crm", "dt"]

res = so.validWordSquare(words)


print(res)
