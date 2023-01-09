class Node:
    def __init__(self, key, next=None) -> None:
        self.key = key
        self.next = next


# own solution, using node represent linktedList

class MyHashSet:

    def __init__(self):
        self.size = 769
        self.bucket = [None for _ in range(self.size)]

    def add(self, key: int) -> None:
        h = self.hash(key)

        cur = self.bucket[h]

        if not cur:
            self.bucket[h] = Node(key)
        else:
            while cur:
                if cur.key == key:
                    return
                else:
                    cur = cur.next
            # does not exist in the chain, append in the beginning
            n = Node(key, self.bucket[h])
            self.bucket[h] = n

    def remove(self, key: int) -> None:
        h = self.hash(key)
        cur = self.bucket[h]
        if not cur:
            return

        if cur.key == key:
            self.bucket[h] = cur.next
        else:
            while cur.next:
                if cur.next.key == key:
                    cur.next = cur.next.next
                    return
                else:
                    cur = cur.next

    def contains(self, key: int) -> bool:
        h = self.hash(key)
        cur = self.bucket[h]

        if not cur:
            return False
        else:
            while cur:
                if cur.key == key:
                    return True
                else:
                    cur = cur.next
            return False

    def hash(self, key):
        return key % self.size

        # Your MyHashSet object will be instantiated and called as such:
        # obj = MyHashSet()
        # obj.add(key)
        # obj.remove(key)
        # param_3 = obj.contains(key)
