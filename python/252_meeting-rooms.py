from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"({self.start}, {self.end})"


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i: (i.start, i.end))
        print(intervals)

        prev = intervals[0].end

        for i in intervals[1:]:

            if i.start < prev:
                print(i.start, prev)
                return False
            else:
                prev = i.end

        return True


# Time:  O(n*log n)
# Space: O(1)
