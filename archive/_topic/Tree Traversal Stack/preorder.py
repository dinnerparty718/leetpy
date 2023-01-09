from typing import Tuple
from Tree.TreeNode import TreeNode


from utils.buildTree import build


def preorder(root: TreeNode):

    res = []
    s = [[False, root]]

    while s:
        top = s[-1]
        if top[0] == True:
            visited, cur = s.pop()

            if cur.right:
                s.append([False, cur.right])

        else:
            top[0] = True
            res.append(top[1].val)
            if top[1].left:
                s.append([False, top[1].left])

    return res


root = build('1,2,3,4,5,,6')


res = preorder(root)

print(res)
