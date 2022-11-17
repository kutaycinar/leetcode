from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        bucket = {}

        for i in range(len(nums)):

            if bucket.get(nums[i]) is None:
                bucket[nums[i]] = 1
            else:
                bucket[nums[i]] += 1

            if bucket[nums[i]] > 1:
                return True

        return False


# Time:  O(n)
# Space: O(n)
