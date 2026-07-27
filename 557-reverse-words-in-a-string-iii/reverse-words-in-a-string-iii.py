class Solution:
    def reverseWords(self, s: str) -> str:
        p = 0
        result = ""
        for i in range(len(s)):
            if s[i] == " ":
                string = list(s[p:i])
                result += "".join(string[::-1])
                result += " "
                p = i + 1
        string = list(s[p:len(s)])
        result += "".join(string[::-1])

        return result

        