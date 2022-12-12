from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        area = 0
        start, end = 0, len(height) - 1

        while start < end:
            area = max(area, (end - start) * min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return area


# Time:  O(n)
# Space: O(1)
