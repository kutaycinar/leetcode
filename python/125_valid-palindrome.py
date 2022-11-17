class Solution:
    def isPalindrome(self, s: str) -> bool:

        # convert to lowercase
        string = ""
        for c in s:
            ascii = ord(c)
            if 64 < ascii < 91:  # range for A-Z
                string += chr(ascii+32)

            if 96 < ascii < 123:  # range for a-z
                string += c

            if 47 < ascii < 58:  # range for 0-9
                string += c

        # check reads forwards and backwards
        p1, p2 = 0, len(string) - 1
        while p1 <= p2:
            if string[p1] != string[p2]:
                return False
            p1 += 1
            p2 -= 1

        return True


# Time:  O(n)
# Space: O(n)
