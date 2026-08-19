class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_pairs = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        
        answer = [""] * len(score)
        
        for rank, (s, original_idx) in enumerate(sorted_pairs, 1):
            if rank == 1:
                answer[original_idx] = "Gold Medal"
            elif rank == 2:
                answer[original_idx] = "Silver Medal"
            elif rank == 3:
                answer[original_idx] = "Bronze Medal"
            else:
                answer[original_idx] = str(rank)
        
        return answer