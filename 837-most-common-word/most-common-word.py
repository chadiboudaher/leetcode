class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for char in "!?',;.":
            paragraph = paragraph.replace(char, " ")
        
        p = paragraph.lower().replace(", ", " ").split()
        freq_count = {}

        for s in p:
            if s not in banned:
                if s in freq_count:
                    freq_count[s] += 1
                else:
                    freq_count[s] = 1
        max_key = max(freq_count, key=freq_count.get)
        return max_key