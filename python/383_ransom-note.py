class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            found = False
            for j in range(len(magazine)):
                if ransomNote[i] == magazine[j]:
                    found = True
                    magazine = magazine[:j] + magazine[j+1:]
                    break
            if not found:
                return False
        return True

    # Time:  O(n * m)
    # Space: O(1)

    # Better time complexity sacrificing memory
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def count(arr):
            dict = {}
            for c in arr:
                if c not in dict:
                    dict[c] = 0
                dict[c] += 1
            return dict

        r = count(ransomNote)
        m = count(magazine)

        for c in r:
            if c not in m or r[c] > m[c]:
                return False

        return True

    # Time:  O(n + m)
    # Space: O(n + m)
