from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # O(n*log n)
        intervals.sort()

        prev_end = intervals[0][1]
        count = 0

        # O(n)
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if prev_end > start:
                count += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end

        return count

# Time:  O(n*log n)
# Space: O(1)
