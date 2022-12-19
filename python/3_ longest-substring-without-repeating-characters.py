import random


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        left, right = 0, 0
        length = 0

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            length = max(length, right-left+1)
            right += 1

        return length

# Time:  O(n)
# Space: O(n)
