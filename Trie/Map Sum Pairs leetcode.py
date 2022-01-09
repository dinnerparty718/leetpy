class Node:
    def __init__(self) -> None:
        self.children = {}
        self.score = 0


class MapSum:

    def __init__(self):
        self.map = {}  # ?? directly store the key and it's val
        self.root = Node()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val

        cur = self.root
        cur.score += delta

        for c in key:
            if c not in cur.children:
                cur.children[c] = Node()

            cur = cur.children[c]
            cur.score += delta

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return 0

            cur = cur.children[c]
        return cur.score
