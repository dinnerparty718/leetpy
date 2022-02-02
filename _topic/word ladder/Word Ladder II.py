import string
from typing import List
from collections import deque, defaultdict

# return all shortest path

# BFS and store the path, if multiple shortest path, a node can not be visited twice
# why add local_visited, draw the graph
# https://www.youtube.com/watch?v=rWd4wScVYxc
#
# https://leetcode.com/problems/word-ladder-ii/discuss/490116/Three-Python-solutions%3A-Only-BFS-BFS%2BDFS-biBFS%2B-DFS


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return []

        res = []

        word_dict = defaultdict(list)

        L = len(beginWord)

        for word in wordList:
            for i in range(L):
                word_dict[word[:i] + '*' + word[i+1:]].append(word)

        # current_word, path, set
        q = deque([[beginWord, [beginWord]]])
        visited = set([beginWord])

        while q and not res:
            size = len(q)
            local_visited = set()

            # current level
            for _ in range(size):
                current_word, path = q.popleft()

                if current_word == endWord:
                    res.append(path)
                    continue

                for i in range(L):
                    new_key = current_word[:i] + '*' + current_word[i+1:]

                    for nei in word_dict[new_key]:
                        if nei not in visited:
                            q.append([nei, path+[nei]])
                            local_visited.add(nei)

            visited = visited.union(local_visited)

        return res


so = Solution()

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log", "cog"]


# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log"]


# beginWord = "hot"
# endWord = "dog"
# wordList = ["hot", "dog"]


beginWord = "qa"
endWord = "sq"
wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb",
            "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]

res = so.findLadders(beginWord, endWord, wordList)


print(res)
