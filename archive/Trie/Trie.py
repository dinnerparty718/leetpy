class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True


trie = Trie()

trie.insert("apple")
print(trie.search("apple"))


print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")

print(trie.search("app"))
