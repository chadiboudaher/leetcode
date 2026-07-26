class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()
        round = 0
        output = 0

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                output = output + round + 1
                round += 1
            else:
                round = 0
        return output