
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = head, head
        i1, i2 = 1, 1

        while p2:
            if i2 // 2 == i1:
                i1 += 1
                p1 = p1.next

            i2 += 1
            p2 = p2.next

        return p1

# Time:  O(n)
# Space: O(1)