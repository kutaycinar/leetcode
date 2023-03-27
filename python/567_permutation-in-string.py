from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        window = Counter(s2[:len(s1)])

        for i in range(len(s1), len(s2)):
            if target == window:
                return True

            window[s2[i]] += 1
            window[s2[i-len(s1)]] -= 1

            if window[s2[i-len(s1)]] == 0:
                window.pop(s2[i-len(s1)])

        return target == window

# Time:  O(n)
# Space: O(m)


print(Solution().checkInclusion("ab", "eidboaoo"))
