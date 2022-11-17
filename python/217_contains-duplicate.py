from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        bucket = {}

        for i in range(len(nums)):
            bucket[nums[i]] = 0

        for i in range(len(nums)):
            bucket[nums[i]] += 1
            if (bucket[nums[i]] > 1):
                return True

        return False

# Time:  O(n)
# Space: O(n)
