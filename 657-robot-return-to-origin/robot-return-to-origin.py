class Solution:
    def judgeCircle(self, moves: str) -> bool:
        origin = [0, 0]
        for move in moves:
            if move == "U":
                origin[1] += 1
            elif move == "D":
                origin[1] -= 1
            elif move == "R":
                origin[0] += 1
            else:
                origin[0] -= 1
        if origin == [0, 0]:
            return True
        return False