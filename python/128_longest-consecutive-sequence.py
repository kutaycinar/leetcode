from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for n in num_set:
            if n - 1 not in num_set:
                len = 1
                while n + len in num_set:
                    len += 1
                max_len = max(len, max_len)
        return max_len


# Time:  O(n)
# Space: O(n)
