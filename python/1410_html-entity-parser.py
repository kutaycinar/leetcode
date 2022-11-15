class Solution:
    def entityParser(self, text: str) -> str:

        i = 0
        while i < len(text):

            if text[i] == "&":

                if text[i:i+6] == "&quot;":
                    text = text[:i] + '"' + text[i+6:]

                elif text[i:i+6] == "&apos;":
                    text = text[:i] + "'" + text[i+6:]

                elif text[i:i+5] == "&amp;":
                    text = text[:i] + "&" + text[i+5:]

                elif text[i:i+4] == "&gt;":
                    text = text[:i] + ">" + text[i+4:]

                elif text[i:i+4] == "&lt;":
                    text = text[:i] + "<" + text[i+4:]

                elif text[i:i+7] == "&frasl;":
                    text = text[:i] + "/" + text[i+7:]

            i += 1

        return text

# Time:  O(n)
# Space: O(1)
