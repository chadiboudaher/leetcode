class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        minLeastIndex = float("inf")

        result = []

        for i in range(len(list1)):
            if list1[i] in list2:
                score = i + list2.index(list1[i])
                if score < minLeastIndex:
                    minLeastIndex = score
                    result = [list1[i]]
                elif score == minLeastIndex:
                    result.append(list1[i])

        return result