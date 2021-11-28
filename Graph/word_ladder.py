from collections import deque
from typing import DefaultDict, List


# time space O(m*m*n) n is the length of the word (m*m) to build the graph
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return 0

        wordList = list(set(wordList))
        w_dict = self.buildDict(wordList)

        cnt = 1
        q = deque([beginWord])
        visited = set([beginWord])

        while q:
            size = len(q)
            for i in range(size):
                w = q.popleft()
                if w == endWord:
                    return cnt

                for i in range(len(w)):
                    s = w[:i] + '_' + w[i+1:]
                    for n in w_dict[s]:
                        if n not in visited:
                            q.append(n)
                            visited.add(n)
            cnt += 1

        return 0

    #  important tricks
    def buildDict(self, wordList: List[str]) -> dict:
        d = DefaultDict(list)
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]
                d[s].append(word)

        return d


beginWord = "hit"
endWord = "cog"


wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

# todo build graph
# find adjacent list

so = Solution()

res = so.ladderLength(beginWord, endWord, wordList)

print()
print(res)
