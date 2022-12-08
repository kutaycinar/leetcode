from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()

        for i, a in enumerate(nums):
            if 0 < i and nums[i-1] == a:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum == 0:
                    output.add((a, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif threesum < 0:
                    l += 1
                elif 0 < threesum:
                    r -= 1

        return list(output)


# Time:  O(n^2)
# Space: O(n)
