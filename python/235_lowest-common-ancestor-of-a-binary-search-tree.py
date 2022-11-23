# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        pointer1 = root
        pointer2 = root
        last_commmon = root

        while True:

            if not pointer1 or not pointer2:
                break

            if pointer1.val != pointer2.val:
                return last_commmon

            last_commmon = pointer1

            if p.val < pointer1.val:
                pointer1 = pointer1.left
            elif p.val > pointer1.val:
                pointer1 = pointer1.right

            if q.val < pointer2.val:
                pointer2 = pointer2.left
            elif q.val > pointer2.val:
                pointer2 = pointer2.right

        return last_commmon

        # Time:  O(log n)
        # Space: O(1)
