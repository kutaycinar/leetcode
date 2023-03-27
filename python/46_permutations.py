from collections import deque
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def build(a):
            if len(a) == len(nums):
                return result.append([*a])

            for x in nums:
                if x not in a:
                    a.append(x)
                    build(a)
                    a.pop()

        build([])

        return result


print(Solution().permute(nums=[1, 2, 3]))
