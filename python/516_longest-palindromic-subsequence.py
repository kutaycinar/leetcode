class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @cache
        def lps(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                return 2 + lps(l+1, r-1)
            else:
                return max(lps(l+1, r), lps(l, r-1))

        return lps(0, len(s) - 1)

# Time:  O(n^2)
# Space: O(n^2)
