class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash1 = {}
        hash2 = {}

        for c in s:
            if hash1.get(c) is None:
                hash1[c] = 1
            hash1[c] += 1

        for c in t:
            if hash2.get(c) is None:
                hash2[c] = 1
            hash2[c] += 1

        return hash1 == hash2


# Time:  O(s+t)
# Space: O(s+t)
