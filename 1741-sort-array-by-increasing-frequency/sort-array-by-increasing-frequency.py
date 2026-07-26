class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        return sorted(nums, key=lambda x: (freq_map[x], -x))

        