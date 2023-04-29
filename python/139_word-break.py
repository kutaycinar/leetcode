from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        word_set = set(wordDict)
        for right in range(1, len(s) + 1):
            for left in range(right):
                if dp[left] and s[left:right] in word_set:
                    dp[right] = True
                    break
        return dp[-1]

# Time:  O(m*n^2)
# Space: O(n)
