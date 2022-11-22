from typing import List


class Solution:
    def search(self, nums: List[int], target: int, counter=0) -> int:

        if len(nums) == 0:
            return -1

        mid = len(nums) // 2

        if nums[mid] == target:
            return counter + mid

        elif nums[mid] > target:
            return self.search(nums[:mid], target, counter)

        elif nums[mid] < target:
            return self.search(nums[mid+1:], target, 1 + counter + mid)


# Time:  O(log n)
# Space: O(1)
