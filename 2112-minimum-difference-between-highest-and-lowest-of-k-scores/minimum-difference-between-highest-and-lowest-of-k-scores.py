class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        if len(nums) <= 1:
            return 0

        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))
