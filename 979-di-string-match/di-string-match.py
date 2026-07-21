class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s)
        out = []
        for i in range(len(s)):
            if s[i] == "I":
                out.append(low)
                low += 1
            else:
                out.append(high)
                high -= 1
        out.append(low)
        return out
            
