from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        keepCount = Counter(words[0])

        for word in words[1:]:
            keepCount &= Counter(word)

        return list(keepCount.elements())