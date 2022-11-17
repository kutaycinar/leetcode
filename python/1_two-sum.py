from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}

        for i, n in enumerate(nums):
            if target-n in hash:
                return [hash[target-n], i]
            hash[n] = i


# Time:  O(n)
# Space: O(n)
