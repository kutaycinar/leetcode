from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        len = 0
        for n in nums:
            if n == 1:
                len += 1
            else:
                len = 0
            max_len = max(len, max_len)
        return max_len


# Time:  O(n)
# Space: O(1)
