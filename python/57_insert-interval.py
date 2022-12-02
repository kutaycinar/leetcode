from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        def overlap(a, b):
            if a[0] <= b[0] <= a[1] or \
               a[0] <= b[1] <= a[1] or \
               b[0] <= a[0] <= b[1] or \
               b[0] <= a[1] <= b[1]:
                return True
            return False

        def merge(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]

        result, added = [], False

        for interval in intervals:
            if not added:
                if overlap(interval, newInterval):
                    newInterval = merge(interval, newInterval)
                    continue
                if newInterval[1] < interval[0]:
                    added = True
                    result.append(newInterval)
                result.append(interval)
            else:
                result.append(interval)

        if not added:
            result.append(newInterval)

        return result


# Time:  O(n)
# Space: O(n)
