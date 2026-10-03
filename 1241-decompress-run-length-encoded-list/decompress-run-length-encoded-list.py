class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(0, len(nums) - 1, 2):
            result.extend([nums[i + 1]] * nums[i])

        return result