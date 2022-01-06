from typing import Tuple
from Tree.TreeNode import TreeNode


from utils.buildTree import build


def postorder(root: TreeNode):

    res = []
    s = [[False, root]]

    while s:
        top = s[-1]
        if top[0] == True:
            visited, cur = s.pop()
            if cur.left:
                s.append([False, cur.left])

        else:
            top[0] = True
            res.append(top[1].val)

            if top[1].right:
                s.append([False, top[1].right])

    res.reverse()

    return res


root = build('1,2,3,4,5,,6')


res = postorder(root)

print(res)
