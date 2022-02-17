from typing import Optional, List
from traversal.dfs_recursion import inOrder, postOrder
from TreeNode import TreeNode

'''
build hashmap for inorder
    h_map = { val: index for index, val in enumerate(inorder)  }
find root ->
    - pop last node from postorder    postorder.pop()
    - pop first node from preorder    pretorder.pop(0)
find left, right children ->  in order          [left children, root, right children]


Bottom up, return root

helper(start, end) -- recursive
    base case
        return None if start > end
        
    root_val = postorder.pop()
    
    root =  Node(root_val)
    
    idx = h_map[root_val]
    
    root.left = helper(start, root_val-1 )
    root.right = helper(root_val+1, end)
    
    return node

 

'''


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # inorder = inorder[:]
        # postorder = postorder[:]

        def helper(start: int, end):

            # if there is no elements to construct subtrees
            if(start > end):
                return None

            val = postorder.pop()
            node = TreeNode(val)

            index = idx_map[val]

            node.right = helper(index + 1, end)
            node.left = helper(start, index - 1)
            return node
        # build a hashmap value -> its index

        idx_map = {val: idx for idx, val in enumerate(inorder)}

        return helper(0, len(inorder)-1)


solution = Solution()

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

result = solution.buildTree(inorder, postorder)


# inOrder()

# inOrder(result)
postOrder(result)

print(postorder)
