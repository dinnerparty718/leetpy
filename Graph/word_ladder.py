from collections import deque
from typing import DefaultDict, List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return 0

        graph = self.buildGraph(wordList)

        if beginWord not in graph:
            return 0

        cnt = 1
        q = deque([beginWord])
        visited = set([beginWord])

        while q:
            size = len(q)
            for i in range(size):
                w = q.popleft()
                if w == endWord:
                    return cnt

                for n in graph[w]:
                    if n not in visited:
                        q.append(n)
                        visited.add(n)

            cnt += 1

        return 0

    def containOneChange(self, w1: str, w2: str) -> bool:
        count = 0
        for i, c in enumerate(w1):
            if c != w2[i]:
                count += 1
                if count > 1:
                    return False
        return count == 1

    def buildGraph(self, wordList: List[str]) -> dict:
        d = DefaultDict(list)

        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                w1 = wordList[i]
                w2 = wordList[j]
                if self.containOneChange(w1, w2):
                    d[w1].append(w2)
                    d[w2].append(w1)

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
