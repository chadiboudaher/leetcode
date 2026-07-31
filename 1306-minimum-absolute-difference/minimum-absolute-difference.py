import math
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min = math.inf

        s_arr = sorted(arr)
        result = []
        for i in range(len(s_arr) - 1):
            diff = s_arr[i + 1] - s_arr[i]
            if diff == min:
                result.append([s_arr[i], s_arr[i + 1]])
            elif diff < min:
                min = diff
                result = []
                result.append([s_arr[i], s_arr[i + 1]])

        return result
        