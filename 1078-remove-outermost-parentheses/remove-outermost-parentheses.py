class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        count = 0
        for ch in s:
            if ch == "(":
                if count > 0:
                    result.append(ch)
                count += 1
            else:
                count -= 1
                if count > 0:
                    result.append(ch)

        return "".join(result)
        