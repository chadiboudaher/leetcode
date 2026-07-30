class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        k, j = 0, 0
        even, odd, result = [], [], []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even[i // 2])
            else:
                result.append(odd[i // 2])
        
        return result
            


        