from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        for s in strs:
            while not s.startswith(pre):
                pre = pre[:-1]
        return pre

# Time:  O(n)
# Space: O(1)
