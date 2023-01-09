from typing import List
import heapq


# todo issue
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.sentences = sentences
        self.times = times

        self.trie = {}

        for idx, sen in enumerate(sentences):
            node = self.trie

            for c in sen:
                if c not in node:
                    newNode = {}
                    newNode['#'] = []
                    node[c] = newNode
                node = node[c]
                node['#'].append(idx)
            node['$'] = idx

        self.curr_search = []
        self.curr_node = self.trie

    def add_to_repo(self, sentense: str):

        # search first, if find

        found = self.search(sentense)

        if found >= 0:
            self.times[found] += 1
        else:
            # add to repo
            self.sentences.append(sentense)
            self.times.append(1)

            index = len(self.sentences) - 1

            node = self.trie

            for c in sentense:
                if c not in node:
                    newNode = {}
                    newNode['#'] = []
                    node[c] = newNode

                node = node[c]
            node['$'] = index

    # not found return -1 else return index

    def search(self, sentense: str) -> int:
        node = self.trie

        for c in sentense:
            if c not in node:
                return -1
            node = node[c]

        return -1 if '$' not in node else node['$']

    def input(self, c: str) -> List[str]:
        if c == '#':
            new_sen = ''.join(self.curr_search)
            self.add_to_repo(new_sen)
            self.curr_search = []
            self.curr_node = self.trie
            return []
        else:
            self.curr_search.append(c)
            if c not in self.curr_node:
                return []
            self.curr_node = self.curr_node[c]

            result = [[-times[idx], sentences[idx]]
                      for idx in self.curr_node['#']]

            heapq.heapify(result)

            res = []

            k = 3

            while k > 0 and result:
                t, s = heapq.heappop(result)
                res.append(s)
                k -= 1

            return res


sentences = ["i love you", "island", "iroman", "i love leetcode"]
times = [5, 3, 2, 2]

obj = AutocompleteSystem(sentences, times)

print(obj.input('i'))
print(obj.input(' '))
print(obj.input('a'))
print(obj.input('#'))


for k, v in obj.trie.items():
    print(k, v)

# print(obj.search('iroman'))
