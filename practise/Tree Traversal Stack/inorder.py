from Tree.TreeNode import TreeNode


from utils.buildTree import build


def inorder(root: TreeNode):
    s = []

    res = []
    while s or root:

        while root:
            s.append(root)
            root = root.left

        cur = s.pop()

        res.append(cur.val)

        root = cur.right

    return res


root = build('1,2,3,4,5,,6')


res = inorder(root)

print(res)
