from typing import List


class Solution:
    # Simple
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        bp = len(nums) // 2
        for n in nums:
            if n not in map:
                map[n] = 0
            map[n] += 1
            if map[n] > bp:
                return n
    # Time:  O(n)
    # Space: O(n)

    # Optimal
    def majorityElement(self, nums: List[int]) -> int:
        major, count = nums[0], 0
        for n in nums:
            if n == major:
                count += 1
            elif count == 0:
                major = n
                count = 1
            else:
                count -= 1
        return major
    # Time:  O(n)
    # Space: O(1)
