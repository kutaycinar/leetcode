# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dim = 0
        def depth(root):
            nonlocal dim
            if not root:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            dim = max(dim, l + r)
            return 1 + max(l, r)
        depth(root)
        return dim

# Time:  O(n)
# Space: O(n)
