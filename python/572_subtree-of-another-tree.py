from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return False
            if same(root, subRoot):
                return True
            return dfs(root.left) or dfs(root.right)

        def same(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return same(p.left, q.left) and same(p.right, q.right)

        return dfs(root)

# Time:  O(m*n)
# Space: O(m+n)
