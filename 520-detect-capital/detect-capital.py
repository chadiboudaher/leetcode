class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (self.isAllCapital(word) or 
                self.isAllLower(word) or 
                self.isFirstLetterCapital(word))
    
    def isAllCapital(self, word: str) -> bool:
        for w in word:
            if ord(w) < 65 or ord(w) > 90:
                return False
        return True
    
    def isAllLower(self, word: str) -> bool:
        for w in word:
            if ord(w) < 97 or ord(w) > 122:
                return False
        return True
    
    def isFirstLetterCapital(self, word: str) -> bool:
        if not (65 <= ord(word[0]) <= 90):
            return False

        for i in range(1, len(word)):
            if not (97 <= ord(word[i]) <= 122):
                return False
        return True