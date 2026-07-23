class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        map = {}
        # build the map of info
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = [1, i, i]
            else:
                map[nums[i]][0] += 1
                map[nums[i]][2] = i


        max_freq = 0
        ans = 0

        for num, data in map.items():
            freq, first, last = data
            if freq > max_freq:
                max_freq = freq
                ans = last - first + 1
            elif freq == max_freq:
                ans = min(ans, last - first + 1)
        
        return ans

        
        