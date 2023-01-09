# double linked list

class Node:
    def __init__(self, key=0, value=0) -> None:
        self.next = None
        self.prev = None
        self.key = key
        self.value = value


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # left -> least recent used
        # right for append new item

        # for append O(1) append
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

        # for O(1) search
        self.cache = {}  # store the key

    # return -1 if not in cache

    def remove(self, node: Node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    # insert to the right, doublelinked list

    def insert(self, node: Node):
        prev = self.right.prev
        next = self.right

        prev.next = node
        node.prev = prev

        node.next = next
        next.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        n = Node(key, value)

        if key in self.cache:
            self.remove(self.cache[key])

        self.insert(n)
        self.cache[key] = n

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)

            del self.cache[lru.key]


lRUCache = LRUCache(2)
