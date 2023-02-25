from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1]:
                j = stack.pop()
                res[j] = i - j

            stack.append(i)

        return res

# Time:  O(n)
# Space: O(n)
