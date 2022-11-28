# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hashset = set()
        dummy = head

        while dummy:
            if dummy in hashset:
                return True
            hashset.add(dummy)
            dummy = dummy.next

        return False

# Time:  O(n)
# Space: O(n)
