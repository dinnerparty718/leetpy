from TreeNode import TreeNode


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


def main() -> None:
    print('inside main fucntion')
    root = TreeNode(4)
    # print(t1) 
    ste = '1,2,0|3,2,4|7,,'

    a =  ste.split('|')
    abc = [ item.split(',') for item in a ]

    print(abc)


if __name__ == '__main__':
    main()
