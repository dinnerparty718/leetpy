
class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev: Node = None
        self.next: Node = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # LRU
        self.left = Node()
        # newly added
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

        self.cache = {}

    def remove(self, node: Node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

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
        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

    def put(self, key: int, value: int) -> None:

        n = Node(key, value)

        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = n

        self.insert(n)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)


capacity = 2
obj = LRUCache(capacity)
