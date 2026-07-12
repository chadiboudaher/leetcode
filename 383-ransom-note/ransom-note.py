class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        '''
        1. Check length of magazine (since repetition is not allowed).
        2. Converting to list and check each **str**.
        '''
        if len(magazine) < len(ransomNote):
            return False

        magazine_list = [0] * 26
        for char in magazine:
            index = ord(char) - ord('a')
            magazine_list[index] += 1

        for char in ransomNote:
            index = ord(char) - ord('a')
            magazine_list[index] -= 1
            if magazine_list[index] < 0:
                return False

        return True
        



        

        