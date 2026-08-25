class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_map = {}

        for c in s:
            if c in my_map:
                my_map[c] += 1
            else:
                my_map[c] = 1

        for i, c in enumerate(s):
            if my_map[c] == 1:
                return i

        return -1
