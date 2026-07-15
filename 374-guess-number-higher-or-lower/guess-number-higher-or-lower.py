# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        high = n
        low = 1
        mid = (high + low) // 2
        while low < high:
            g = guess(mid)
            if g == -1:
                high = mid - 1
            elif g == 1:
                low = mid + 1
            else: 
                break
            mid = (high + low) // 2
        return mid
        