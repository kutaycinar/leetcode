from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequency of tasks
        freq = Counter(tasks)
        # maximum frequent task
        max_freq = max(freq.values())
        # number of maximum frequent tasks
        num_max_freq = len([v for v in freq.values() if v == max_freq])
        # number of blanks between maximum frequent tasks
        blanks = max_freq - 1
        # number of empty spaces within the blank
        spaces = 1 + n - num_max_freq
        # total number of available blank spaces
        spots = blanks * spaces
        # remaning number of tasks
        remain = freq.total() - (num_max_freq * max_freq)
        # return number of max frequent tasks + number of spots (or remaning tasks if more)
        return num_max_freq * max_freq + max(spots, remain)

# Time:  O(n)
# Space: O(1)
