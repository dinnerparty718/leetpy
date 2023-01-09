from naryTree import Node, sample_NaryTree2

from collections import deque


# own
# leetcode levelorder

# todo check leetcode method
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """

        res = []

        if not root:
            return ''

        q = deque([root])

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()

                if not node:
                    res.append('')
                else:
                    res.append(str(node.val))

                    if node.children:
                        q.extend(node.children)

                    q.append(None)

            if res[-1] != '':
                res.append('')

        i = len(res)-1

        while res[i] == '':
            i -= 1

        return ','.join(res[0:i+1])

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """

        if not data:
            return None

        nodes = data.split(',')

        root = Node(int(nodes[0], []))

        i = 1

        q = deque([root])

        while q:
            parent = q.popleft()

            if not parent:
                continue

            children = []

            # skip the first one
            i += 1

            while i < len(nodes) and nodes[i] != '':
                if nodes[i] == '':
                    n = None
                else:
                    n = Node(int(nodes[i], []))
                children.append(n)
                i += 1

            if children:
                parent.children = children
                q.extend(children)
            else:
                q.append(None)

        return root


root = sample_NaryTree2()

codec = Codec()


s = codec.serialize(root)

print(s)
root2 = codec.deserialize(s)

s2 = codec.serialize(root2)

print(s2)
