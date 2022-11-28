# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        p1, p2 = None, head

        while p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp

        return p1

# Time:  O(n)
# Space: O(1)
