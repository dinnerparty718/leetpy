
# each bucket is a linked list , a list in python
# operation happens in bucket
class Bucket:
    def __init__(self) -> None:
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]


class MyHashMap:

    def __init__(self):
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.key_space
        return self.hash_table[hash_key].update(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)

        # Your MyHashMap object will be instantiated and called as such:
        # obj = MyHashMap()
        # obj.put(key,value)
        # param_2 = obj.get(key)
        # obj.remove(key)


# own linked list, waste space since each slot has empty linkedlist initialize
class Linked_list:
    def __init__(self) -> None:
        self.head = Node(0, 0)
        self.size = 0

    def put(self, key, value):
        cur = self.head.next

        # found
        while cur:
            if cur.key == key:
                cur.value = value
                return
            else:
                cur = cur.next

        # not found
        # add to front
        to_add = Node(key, value)
        to_add.next = self.head.next
        self.head.next = to_add
        self.size += 1

    def get(self, key):
        # not found return 1
        cur = self.head.next

        while cur:
            if cur.key == key:
                return cur.value
            else:
                cur = cur.next

        # curr = None not found
        return -1

    def remove(self, key):
        # found the previous node
        cur = self.head

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                self.size -= 1
            else:
                cur = cur.next

        # key not found


class Node:
    def __init__(self, key, value) -> None:
        self.value = value
        self.key = key
        self.next = None


class MyHashMap2:

    def __init__(self):
        self.key_space = 2069
        self.hash_table = [Linked_list() for i in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.key_space
        return self.hash_table[hash_key].put(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)

    def hash_function(self, key):
        return key % self.key_space
        # Your MyHashMap object will be instantiated and called as such:
        # obj = MyHashMap()
        # obj.put(key,value)
        # param_2 = obj.get(key)
        # obj.remove(key)


# todo use node and chaining node
class MyHashMap3:

    def __init__(self):
        #        self.size = 10 ** 6 + 1
        self.capacity = 2069
        self.bucket = [None for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:

        # self.remove(key)
        # h = self.hash_function(key)
        # node = Node(key, value)
        # node.next = self.data[h]
        # self.data[h] = node
        h = self.hash_function(key)
        if not self.bucket[h]:
            self.bucket[h] = Node(key, value)
        else:
            cur = self.bucket[h]

            while cur:
                if cur.key == key:
                    cur.value = value
                    return
                else:
                    cur = cur.next

            n = Node(key, value)
            n.next = self.bucket[h]
            self.bucket[h] = n

    def get(self, key: int) -> int:
        h = self.hash_function(key)
        if not self.bucket[h]:
            return -1
        else:
            cur = self.bucket[h]
            while cur:
                if cur.key == key:
                    return cur.value
                else:
                    cur = cur.next

            return -1

    def remove(self, key: int):
        h = self.hash_function(key)
        node = self.bucket[h]
        if not node:
            return
        if node.key == key:
            # !
            self.bucket[h] = node.next
            return
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

        # Your MyHashMap object will be instantiated and called as such:
        # obj = MyHashMap()
        # obj.put(key,value)
        # param_2 = obj.get(key)
        # obj.remove(key)

    def hash_function(self, key):
        return key % self.capacity


my_hash = MyHashMap3()

my_hash.put(1, 0)
# my_hash.put(2070, 2)

my_hash.remove(2070)
