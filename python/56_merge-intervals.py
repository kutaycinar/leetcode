from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            prev, curr = merged.pop(), intervals[i]
            if prev[1] >= curr[0]:
                start = min(prev[0], curr[0])
                end = max(prev[1], curr[1])
                merged.append([start, end])
            else:
                merged.append(prev)
                merged.append(curr)

        return merged

# Time:  O(n*log n)
# Space: O(n)
