class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_count = {}

        for i in range(len(arr)):
            if arr[i] in freq_count:
                freq_count[arr[i]] += 1
            else:
                freq_count[arr[i]] = 1

        return len(set(freq_count.values())) == len(list(freq_count.values()))
        