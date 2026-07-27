class Solution:
    def reverseWords(self, s: str) -> str:
        p = 0
        result = ""
        for i in range(len(s)):
            if s[i] == " ":
                result += "".join(s[p:i][::-1])
                result += " "
                p = i + 1
        result += "".join(s[p:len(s)][::-1])

        return result

        