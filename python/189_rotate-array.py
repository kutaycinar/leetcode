from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        size = len(nums)
        temp = nums.copy()

        for i in range(size):
            nums[(i+k) % size] = temp[i]

# Time:  O(n)
# Space: O(n)
