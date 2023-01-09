from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        endOfWord = '$'

        for word in words:
            cur = trie
            for w in word:
                if w not in cur:
                    cur[w] = {}
                cur = cur[w]

            cur[endOfWord] = word

        m = len(board)
        n = len(board[0])

        matched_words = []

        def backtrack(i: int, j: int, parent: dict):

            letter = board[i][j]
            currNode = parent[letter]

            #! also remove the word in the trie to avoid duplicated
            word_matched = currNode.pop(endOfWord, False)

            if word_matched:
                matched_words.append(word_matched)

            # before exploration , mark cell as visited
            board[i][j] = '#'

            # explore

            for (I, J) in (i+1, j), (i-1, j), (i, j-1), (i, j+1):
                if 0 <= I < m and 0 <= J < n and board[I][J] in currNode:
                    backtrack(I, J, currNode)

            board[i][j] = letter

            # optimization
            if not currNode:
                parent.pop(letter)

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtrack(i, j, trie)

        return matched_words


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
         ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]


so = Solution()

res = so.findWords(board, words)

print(res)
