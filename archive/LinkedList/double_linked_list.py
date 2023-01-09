class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return - 1

        if index <= self.size / 2:
            print('getting from head')
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
            return curr.val

        else:
            # get from tail
            print('getting from tail')
            curr = self.tail

            for _ in range(self.size - index):
                curr = curr.prev
            return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:

        if index < 0:
            index = 0

        if index > self.size:
            return

        # add from beggning
        # add from end
        to_add = Node(val)

        if index <= self.size / 2:

            print('add from head')
            pred = self.head

            for _ in range(index):
                pred = pred.next
            succ = pred.next

        else:
            succ = self.tail
            print('add from tail')

            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        to_add.next = succ
        succ.prev = to_add

        to_add.prev = pred
        pred.next = to_add

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index > self.size - 1:
            return

        if index <= self.size / 2:
            print('delete from head')

            pred = self.head

            for _ in range(index):
                pred = pred.next

            succ = pred.next.next

        else:
            print('delete from tail')

            succ = self.tail

            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev

        pred.next = succ
        succ.prev = pred

        self.size -= 1


lst = MyLinkedList()

lst.addAtHead(1)
lst.addAtTail(3)
lst.addAtIndex(1, 2)
lst.deleteAtIndex(0)

# print(lst.tail.prev.prev.val)

print(lst.size)
