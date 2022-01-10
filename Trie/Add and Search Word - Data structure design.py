class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.endOfWord = True

    #! important a node can contain dot '.'

    def search(self, word: str) -> bool:

        def search_in_node(word: str, node: TrieNode) -> bool:
            for i, c in enumerate(word):
                if c not in node.children:
                    if c == '.':
                        for x in node.children:  # chidren is a map, x is a key
                            if search_in_node(word[i+1:], node.children[x]):
                                return True
                    return False
                else:
                    node = node.children[c]

            return node.endOfWord

        return search_in_node(word, self.root)
