from typing import List
from collections import deque, defaultdict


# leetcode


# time O(n^2 m)  n number of node   at most could have n^2 edegs
# m is the lengh of the each words

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # all the words are same length
        L = len(beginWord)

        all_combi_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                key = word[:i] + '*' + word[i+1:]
                all_combi_dict[key].append(word)

        # queue for BFS

        queue = deque([(beginWord, 1)])
        # visited = {beginWord: True}
        visited = set([beginWord])

        while queue:
            current_word, level = queue.popleft()

            for i in range(L):
                itermediate_word = current_word[:i] + '*' + current_word[i+1:]

                # next state
                for word in all_combi_dict[itermediate_word]:
                    if word == endWord:
                        return level+1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level+1))
                all_combi_dict[itermediate_word] = []

        return 0


# own 2nd time
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0
        if endWord not in wordList:
            return 0
        q = deque([beginWord])
        visited = set([beginWord])

        # build graph

        graph = defaultdict(list)

        for word in wordList:
            for idx in range(len(word)):
                key = word[:idx] + '*' + word[idx+1:]
                graph[key].append(word)

        res = 1

        while q:

            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for i in range(len(word)):
                    key = word[:i] + '*' + word[i+1:]
                    for nei in graph[key]:
                        if nei not in visited:
                            q.append(nei)
                            # faster than adding to the begining
                            visited.add(nei)

            res += 1

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log"]


# beginWord = "hot"
# endWord = "dog"
# wordList = ["hot", "dog"]

so = Solution()

res = so.ladderLength(beginWord, endWord, wordList)

print(res)
