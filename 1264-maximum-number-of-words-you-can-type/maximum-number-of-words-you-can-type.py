class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        count = 0
        
        for word in words:
            can_type = True
            for char in brokenLetters:
                if char in word:
                    can_type = False
                    break
            if can_type:
                count += 1
                
        return count