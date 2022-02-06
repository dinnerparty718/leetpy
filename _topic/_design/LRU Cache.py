# double linked list
class Node:
    def __init__(self, key=0) -> None:
        self.next = None
        self.prev = None
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass
