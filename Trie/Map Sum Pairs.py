

# own Trie with recursive


class Node:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False
        self.val = 0


class MapSum:

    def __init__(self):
        self.root = Node()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:

            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.endOfWord = True
        cur.val = val

    def sum(self, prefix: str) -> int:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return 0
            cur = cur.children[c]

        def helper(node: Node) -> int:
            if not node.children:
                return node.val

            total = 0
            for ch in node.children.values():
                total += helper(ch)

            return total + node.val

        return helper(cur)


obj = MapSum()
obj.insert('apple', 3)
print(obj.sum("ap"))
obj.insert("app", 2)
print(obj.sum("ap"))
