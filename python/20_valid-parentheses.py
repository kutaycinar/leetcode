class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:

            match c:
                case "(" | "[" | "{":
                    stack.append(c)

                case ")":
                    if len(stack) == 0 or stack.pop() != "(":
                        return False

                case "]":
                    if len(stack) == 0 or stack.pop() != "[":
                        return False

                case "}":
                    if len(stack) == 0 or stack.pop() != "{":
                        return False

        return True if len(stack) == 0 else False


# Time:  O(n)
# Space: O(n)
