from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        total = 0
        for i in range(n):
            total += i + 1

        for n in nums:
            total -= n

        return total


# Time:  O(n)
# Space: O(1)
