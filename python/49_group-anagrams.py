from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash = defaultdict(list)

        for s in strs:
            keys = [0] * 26
            for c in s:
                keys[ord(c) - ord('a')] += 1
            hash[tuple(keys)].append(s)

        return list(hash.values())


# Time:  O(m*n)
# Space: O(m)
