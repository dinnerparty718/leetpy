class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.size = 0

    def get(self, index: int) -> int:

        if index >= self.size or index < 0:
            return -1

        curr = self.head

        for idx in range(index + 1):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:

        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        curr = self.head

        for idx in range(index):
            curr = curr.next

        n = Node(val)
        n.next = curr.next
        curr.next = n
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        if index >= self.size or index < 0:
            return

        curr = self.head

        for idx in range(index):
            curr = curr.next

        curr.next = curr.next.next

        self.size -= 1

        # Your MyLinkedList object will be instantiated and called as such:
        # obj = MyLinkedList()
        # param_1 = obj.get(index)
        # obj.addAtHead(val)
        # obj.addAtTail(val)
        # obj.addAtIndex(index,val)
        # obj.deleteAtIndex(index)


lst = MyLinkedList()

lst.addAtHead(4)
lst.addAtTail(5)

lst.deleteAtIndex(0)

print(lst.get(0))
print(lst.size)
