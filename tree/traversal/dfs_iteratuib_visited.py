from typing import Optional


from Tree.TreeNode import TreeNode
from typing import List
from utils.buildTree import build


class Solution:

    # 1 append 2 left 3 right
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack, r = [[root, 0]], []

        while stack:
            top = stack[-1]

            # if visited
            if top[1]:
                stack.pop()
                if top[0].right:
                    stack.append([top[0].right, 0])
            else:
                r.append(top[0].val)

                top[1] = 1

                if top[0].left:
                    stack.append([top[0].left, 0])

        return r

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack, r = [[root, 0]], []

        while stack:
            top = stack[-1]

            # if visited
            if top[1]:
                stack.pop()
                if top[0].right:
                    stack.append([top[0].right, 0])
            else:
                r.append(top[0].val)

                top[1] = 1

                if top[0].left:
                    stack.append([top[0].left, 0])

        return r


def main():
    so = Solution()
    root = build('1,2,3,4,5,6')

    res = so.preorderTraversal(root)
    print(res)


if __name__ == '__main__':
    main()
