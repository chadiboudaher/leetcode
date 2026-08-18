class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = int("".join(map(str, digits)))
        res += 1
        return [int(i) for i in str(res)]