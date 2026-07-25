class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or char != s[i]:
                    return strs[0][:i]
        return strs[0]