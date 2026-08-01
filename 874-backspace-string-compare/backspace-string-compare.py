class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s, stack_t = [], []

        for i in range(len(s)):
            if s[i] != "#":
                stack_s.append(s[i])
            elif s[i] == "#" and len(stack_s) !=0:
                stack_s.pop()
            else:
                continue
        for i in range(len(t)):
            if t[i] != "#":
                stack_t.append(t[i])
            elif t[i] == "#" and len(stack_t) != 0:
                stack_t.pop()
            else:
                continue
        
        return stack_s == stack_t
