class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                print(s[p1], p1, p2)
                p1 += 1
            p2 += 1
        return p1 == len(s)


# Time:  O(n + m)
# Space: O(1)
