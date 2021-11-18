# Definition for a binary tree node.
from typing import List, Optional
from utils.buildTree import build
from Tree.TreeNode import TreeNode
from collections import defaultdict


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        nodes = defaultdict(list)

        # right track :) inOrder or postOrder
        def subTreeSt(node: TreeNode) -> str:
            if not node:
                return 'null'

            res = ','.join([str(node.val), subTreeSt(
                node.left), subTreeSt(node.right)])

            nodes[res].append(node)

            return res

        subTreeSt(root)

        # for k, v in nodes.items():
        #     print(k, v)

        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]


so = Solution()
tr = '1,2,3,4,,2,4,,,4'

root = build(tr)

res = so.findDuplicateSubtrees(root)


for tr in res:
    print(tr.val)
