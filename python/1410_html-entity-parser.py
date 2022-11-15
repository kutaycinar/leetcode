class Solution:
    def entityParser(self, text: str) -> str:

        codex = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }

        i = 0
        while i < len(text):

            if text[i] == "&":
                for x in codex:
                    if text[i:i+len(x)] == x:
                        text = text[:i] + codex[x] + text[i+len(x):]
                        break

            i += 1

        return text

# Time:  O(n)
# Space: O(1)
