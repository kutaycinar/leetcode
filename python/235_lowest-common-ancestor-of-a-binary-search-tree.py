# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ps = []
        qs = []

        pointer = root
        while pointer.val != p.val:
            ps.append(pointer)
            if p.val < pointer.val:
                pointer = pointer.left
            else:
                pointer = pointer.right
        ps.append(pointer)

        pointer = root
        while pointer.val != q.val:
            qs.append(pointer)
            if q.val < pointer.val:
                pointer = pointer.left
            else:
                pointer = pointer.right
        qs.append(pointer)

        last = None
        length = range(len(qs)) if len(ps) > len(qs) else range(len(ps))
        for i in length:
            if ps[i].val == qs[i].val:
                last = ps[i]
            else:
                break

        return last

    # Time:  O(log n)
    # Space: O(log n)
