class Solution:
    def maxDepth(self, s: str) -> int:
        currentDepth = 0
        maxDepth = 0

        for i in range(len(s)):
            if s[i] == "(":
                currentDepth += 1
            elif s[i] == ")":
                if currentDepth > maxDepth:
                    maxDepth = currentDepth
                currentDepth -= 1

        return maxDepth