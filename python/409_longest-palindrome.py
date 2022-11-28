class Solution:
    def longestPalindrome(self, s: str) -> int:

        dict = {}

        for c in s:
            if c not in dict:
                dict[c] = 0
            dict[c] += 1

        evens, odd = 0, 0

        for x in dict:

            if dict[x] % 2 == 0:
                evens += dict[x]
            else:
                if not odd:
                    odd = dict[x]
                else:
                    evens += dict[x] - 1

        return evens + odd

# Time:  O(n)
# Space: O(n)