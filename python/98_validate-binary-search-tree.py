from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def traverse(node):
            if not node:
                return []
            return traverse(node.left) + [node.val] + traverse(node.right)

        inorder = traverse(root)

        for i in range(1, len(inorder)):
            if not inorder[i] > inorder[i-1]:
                return False
        
        return True


print(Solution().isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))))
