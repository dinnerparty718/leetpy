from typing import List


# leet code solution with backtrack
# todo valid word square

class Solution:

    #! keep track of word index in each node
    def buildTrie(self, words):
        self.trie = {}

        for wordIndex, word in enumerate(words):
            node = self.trie
            for char in word:
                if char in node:
                    node = node[char]
                else:
                    newNode = {}
                    newNode['#'] = []
                    node[char] = newNode
                    node = newNode
                node['#'].append(wordIndex)

        for k, v in self.trie.items():
            print(k, v)

    def getWordsWIthPrefix(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        return [self.words[wordIndex] for wordIndex in node['#']]

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words = words
        self.N = len(words[0])

        self.buildTrie(self.words)

        results = []
        word_squares = []

        for word in words:
            word_squares = [word]
            self.backtrack(1, word_squares, results)

        return results

    def backtrack(self, step, word_squares, results):
        if step == self.N:
            results.append(word_squares[:])
            return

        prefix = ''.join([word[step] for word in word_squares])
        # print(prefix)

        for candidate in self.getWordsWIthPrefix(prefix):
            word_squares.append(candidate)
            self.backtrack(step+1, word_squares, results)
            word_squares.pop()


words = ["area", "lead", "wall", "lady", "ball"]


so = Solution()

res = so.wordSquares(words)


# print(res)
