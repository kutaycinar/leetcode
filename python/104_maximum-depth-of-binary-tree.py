# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        # depth-first-search
        def dfs(node):
            if not node:
                return 0
            return 1 + max(dfs(node.left), dfs(node.right))

        # breath-first-search
        def bfs(node):
            queue = deque([])
            queue.append(node)
            level = 0
            while queue:
                for _ in range(len(queue)):
                    n = queue.popleft()
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
                level += 1
            return level

        # iterative depth-first-search
        def dfs_iterative(node):
            stack = []
            stack.append([node, 1])
            level = 0
            while stack:
                n, depth = stack.pop()
                if n.right:
                    stack.append([n.right, depth+1])
                if n.left:
                    stack.append([n.left, depth+1])
                if not n.left and not n.right:
                    level = max(depth, level)
            return level

        return (dfs(root) + bfs(root) + dfs_iterative(root)) // 3

# Time:  O(n)
# Space: O(n)
