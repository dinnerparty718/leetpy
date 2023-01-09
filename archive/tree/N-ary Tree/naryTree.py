
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def sample_NaryTree():

    root = Node(1)

    a = Node(2)
    b = Node(3)
    c = Node(4)

    root.children = [a, b, c]

    d = Node(5)
    e = Node(6)
    f = Node(7)

    a.children = [d, e, f]

    h = Node(8)
    i = Node(9)
    j = Node(10)

    d.children = [h, i, j]

    return root


def sample_NaryTree2():

    root = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    root.children = [n2, n3, n4, n5]

    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)

    n3.children = [n6, n7]
    n4.children = [n8]
    n5.children = [n9, n10]

    n11 = Node(11)
    n12 = Node(12)
    n13 = Node(13)
    n14 = Node(14)

    n7.children = [n11]
    n8.children = [n12]
    n9.children = [n13]
    n11.children = [n14]

    return root
