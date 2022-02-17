from typing import List
import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        osf = ''
        for c in word:
            if c not in node.children:
                break
            node = node.children[c]
            osf += c
            if node.isWord:
                return osf
        return word


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()
        for words in dict:
            trie.insert(words)
        res = ''
        for sent in sentence.split():
            if res:
                res += ' '
            res += trie.search(sent)
        return res


dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"

dictionary = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"


so = Solution()

res = so.replaceWords(dictionary, sentence)


print(res)
