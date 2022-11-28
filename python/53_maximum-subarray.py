from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, max = 0, nums[0]
        for n in nums:
            sum += n
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max


# Time:  O(n)
# Space: O(1)
