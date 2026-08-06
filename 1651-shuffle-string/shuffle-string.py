class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [""] * len(s)

        for i, ch in enumerate(s):
            result[indices[i]] = ch
        
        return "".join(result)
        