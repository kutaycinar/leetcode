class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        m = max(len(word1), len(word2))
        res = []
        for i in range(n):
            res.append(word1[i] + word2[i])
        if len(word1) > len(word2):
            res.append(word1[n:m])
        if len(word2) > len(word1):
            res.append(word2[n:m])
        return res


# Time:  O(n + m)
# Space: O(n + m)
