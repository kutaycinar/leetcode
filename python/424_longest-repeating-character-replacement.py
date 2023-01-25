from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while len(range(l, r)) + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, len(range(l, r)) + 1)


# Time:  O(n)
# Space: O(26)
