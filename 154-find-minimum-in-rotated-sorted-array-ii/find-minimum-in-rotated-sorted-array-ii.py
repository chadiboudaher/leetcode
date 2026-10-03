class Solution:
    def findMin(self, nums: list[int]) -> int:
        minNum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < minNum:
                minNum = nums[i]
        
        return minNum