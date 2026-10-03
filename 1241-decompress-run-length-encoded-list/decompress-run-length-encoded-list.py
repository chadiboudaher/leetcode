class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        result = []
        currentList = 0
        for i in range(0, len(nums) - 1, 2):
            currentList = [nums[i + 1]] * nums[i]
            result.extend(currentList)

        return result