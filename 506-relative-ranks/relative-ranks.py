class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = [0] * len(score)
        sorted_score = sorted(score, reverse=True)

        map = {}

        for i in range(len(score)):
            if score[i] not in map:
                map[score[i]] = [i+1, sorted_score.index(score[i])+1]

        for val, key in map.items():
            if key[1] == 1:
                answer[key[0]-1] = "Gold Medal"
            elif key[1] == 2:
                answer[key[0]-1] = "Silver Medal"
            elif key[1] == 3:
                answer[key[0]-1] = "Bronze Medal"
            else:
                answer[key[0]-1] = str(key[1])

        return answer