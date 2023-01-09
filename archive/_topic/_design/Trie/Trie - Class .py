
# implemented both in Class or as a nested object

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        node = self.root

        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root

        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]

        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]

        return True


trie = Trie()

trie.insert('apple')
