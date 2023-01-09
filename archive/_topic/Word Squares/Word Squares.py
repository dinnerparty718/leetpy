from typing import List
# https://leetcode.com/problems/word-squares/solution/


#  backtrack using trie
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        n = len(words[0])
        res = []

        contains = '#'

        def buildTrie(words: List[str]):
            trie = {}
            #! better to idx instead of word
            for idx, word in enumerate(words):
                cur = trie

                for w in word:
                    if w not in cur:
                        cur[w] = {}
                        cur[w][contains] = []

                    cur = cur[w]

                    cur[contains].append(word)

            return trie

        trie = buildTrie(words)

        def get_words_from_trie(prefix: str) -> List[str]:
            cur = trie

            for char in prefix:
                if char not in cur:
                    return []
                cur = cur[char]

            return cur[contains]

        def getWordsByPrefix(prefix: str) -> List[str]:
            n = len(prefix)
            res = []

            for word in words:
                if word[:n] == prefix:
                    res.append(word)

            return res

        def backtrack(index: int, curr: List[List[str]]):
            if index == n:
                res.append(curr[:])
                return

            prefix = ''

            for row in range(index):
                prefix += curr[row][index]

            # candidates = getWordsByPrefix(prefix)
            candidates = get_words_from_trie(prefix)

            if candidates:
                for can in candidates:
                    curr.append(can)
                    backtrack(index+1, curr)
                    curr.pop()

        for word in words:
            curr = [word]
            backtrack(1, curr)

        return res


so = Solution()
words = ["ball", "area", "lead", "wall", "lady"]

# words = ["abat", "baba", "atan", "atal"]

res = so.wordSquares(words)


print(res)
