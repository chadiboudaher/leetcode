import math

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        res = 0
        if len(nums) <= 3:
            return math.prod(nums)

        sorted_nums = sorted(nums)

        res = max(
                sorted_nums[0] * sorted_nums[1] * sorted_nums[-1],
                sorted_nums[-1] * sorted_nums[-2] * sorted_nums[-3]
            )

        return res