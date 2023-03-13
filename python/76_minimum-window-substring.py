from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        s_count = Counter()  # window
        t_count = Counter(t)  # occurances
        print(t_count)

        l, res = 0, []
        for r, c in enumerate(s):
            s_count[c] += 1

            # check intersection
            if s_count & t_count != t_count:
                continue

            # minimize window
            while l <= r:
                s_count[s[l]] -= 1
                l += 1

                print(s[l:r+1])
                if s_count & t_count == t_count:
                    continue

                # window no longer valid, append last valid window
                res.append(s[l-1:r+1])
                break

        return min(res, key=len) if res else ""
