class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        count = 0

        start = max(0, n - k)
        end = n + k + 1
        
        for x in range(start, end):
            if (n & x) == 0:
                count += x

        return count