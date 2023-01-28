from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        print("hello")
        a = nums[0]
        b = nums[2]
        print(a + b)

        return None

        hash = {}

        for i, n in enumerate(nums):
            if target-n in hash:
                return [hash[target-n], i]
            hash[n] = i


# Time:  O(n)
# Space: O(n)

Solution().twoSum([1,2,4,5], 7)
